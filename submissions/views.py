import html
import os
import re

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.core.cache import cache

from .models import Submission


def sanitize_input(text: str, max_length: int = None) -> str:
    """
    Sanitize user input: strip whitespace, escape HTML, limit length.
    """
    if not text:
        return ""
    text = text.strip()
    if max_length:
        text = text[:max_length]
    # Escape HTML to prevent XSS
    text = html.escape(text)
    return text


def validate_receipt_code(code: str) -> bool:
    """
    Validate receipt code format: should be digits-only, format XXXXX-XXXXX.
    """
    if not code:
        return False
    # Remove dashes for validation
    cleaned = code.replace("-", "")
    # Should be exactly 10 digits
    return bool(re.match(r"^\d{10}$", cleaned))


@require_http_methods(["GET", "POST"])
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "submissions/home.html")


@require_http_methods(["GET", "POST"])
def submit(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "submissions/submit.html")

    # Validate access code - check against HR access codes
    access_code = (request.POST.get("access_code") or "").strip()
    
    # Check if code matches any HR access code
    from .models import HrAccessCode
    from django.db import OperationalError, ProgrammingError
    
    hr_code = None
    try:
        # Try to query HR access codes (only works if migrations have run)
        hr_code = HrAccessCode.objects.get(access_code=access_code, is_active=True)
    except HrAccessCode.DoesNotExist:
        # Code doesn't match any HR access code
        # Fallback to old COMPANY_ACCESS_CODE for backward compatibility
        if hasattr(settings, 'COMPANY_ACCESS_CODE') and access_code == settings.COMPANY_ACCESS_CODE:
            pass  # Allow old code to work
        else:
            return render(
                request,
                "submissions/submit.html",
                {
                    "error": "Invalid access code. Please check and try again.",
                    "access_code": access_code,  # Preserve input
                },
                status=400,
            )
    except (OperationalError, ProgrammingError):
        # Table doesn't exist yet - migrations haven't run (SQLite or PostgreSQL)
        # Fallback to old COMPANY_ACCESS_CODE for backward compatibility
        if hasattr(settings, 'COMPANY_ACCESS_CODE') and access_code == settings.COMPANY_ACCESS_CODE:
            pass  # Allow old code to work
        else:
            return render(
                request,
                "submissions/submit.html",
                {
                    "error": "Invalid access code. Please check and try again.",
                    "access_code": access_code,  # Preserve input
                },
                status=400,
            )

    # Validate and sanitize inputs
    submission_type = (request.POST.get("type") or "").strip()
    title = sanitize_input(request.POST.get("title") or "", max_length=255)
    body = sanitize_input(request.POST.get("body") or "", max_length=5000)

    errors = []

    if submission_type not in Submission.SubmissionType.values:
        errors.append("Please select a valid submission type.")

    if not title or len(title) < 3:
        errors.append("Title must be at least 3 characters long.")

    if not body or len(body) < 10:
        errors.append("Description must be at least 10 characters long.")

    if len(body) > 5000:
        errors.append("Description is too long (maximum 5000 characters).")

    if errors:
        return render(
            request,
            "submissions/submit.html",
            {
                "error": " ".join(errors),
                "access_code": access_code,
                "submission_type": submission_type,
                "title": html.unescape(title) if title else "",
                "body": html.unescape(body) if body else "",
            },
            status=400,
        )

    # Create submission
    try:
        # Only include hr_access_code if it exists
        submission_kwargs = {
            "type": submission_type,
            "title": html.unescape(title),  # Store unescaped in DB
            "body": html.unescape(body),  # Store unescaped in DB
        }
        if hr_code:
            submission_kwargs["hr_access_code"] = hr_code
        
        s = Submission.create_with_unique_receipt(**submission_kwargs)
    except Exception as e:
        # Log the actual error for debugging - print to stdout so Railway captures it
        import logging
        import traceback
        import sys
        
        logger = logging.getLogger(__name__)
        error_msg = f"Error creating submission: {type(e).__name__}: {e}"
        traceback_str = traceback.format_exc()
        
        # Log to logger
        logger.error(error_msg)
        logger.error(traceback_str)
        
        # Also print to stdout/stderr so Railway captures it
        print(f"ERROR: {error_msg}", file=sys.stderr, flush=True)
        print(traceback_str, file=sys.stderr, flush=True)
        
        # If DEBUG is on, show more details
        if settings.DEBUG:
            return render(
                request,
                "submissions/submit.html",
                {
                    "error": f"Error: {error_msg}. Check logs for details.",
                    "access_code": access_code,
                },
                status=500,
            )
        
        return render(
            request,
            "submissions/submit.html",
            {
                "error": "An error occurred while submitting. Please try again.",
                "access_code": access_code,
            },
            status=500,
        )

    # Notify HR - send to specific HR if code was used, otherwise use default
    recipient_emails = []
    
    if hr_code:
        # Send to the specific HR whose code was used
        hr_email = hr_code.get_notification_email()
        if hr_email:
            recipient_emails = [hr_email]
    elif settings.HR_NOTIFY_EMAILS:
        # Fallback to default HR emails for old access codes
        recipient_emails = settings.HR_NOTIFY_EMAILS
    
    if recipient_emails:
        try:
            send_mail(
                subject=f"New anonymous submission: {s.get_type_display()}",
                message=(
                    f"Type: {s.get_type_display()}\n"
                    f"Title: {s.title}\n"
                    f"Receipt: {s.receipt_code}\n"
                    f"Submitted: {s.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
                    f"View in admin: {request.build_absolute_uri(f'/admin/submissions/submission/{s.id}/change/')}\n"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipient_emails,
                fail_silently=True,
            )
        except Exception:
            # Don't fail submission if email fails
            pass

    request.session["last_receipt_code"] = s.receipt_code
    return redirect("submissions:submitted")


def submitted(request: HttpRequest) -> HttpResponse:
    receipt_code = request.session.get("last_receipt_code")
    return render(request, "submissions/submitted.html", {"receipt_code": receipt_code})


@require_http_methods(["GET", "POST"])
def status_lookup(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "submissions/status_lookup.html")

    receipt_code = (request.POST.get("receipt_code") or "").strip().replace(" ", "")

    # Validate format
    if not validate_receipt_code(receipt_code):
        return render(
            request,
            "submissions/status_lookup.html",
            {
                "error": "Invalid receipt code format. It should be 10 digits (e.g., 12345-67890).",
                "receipt_code": receipt_code,
            },
            status=400,
        )

    try:
        submission = Submission.objects.select_related("hr_response").get(receipt_code=receipt_code)
    except Submission.DoesNotExist:
        return render(
            request,
            "submissions/status_lookup.html",
            {
                "error": "Receipt code not found. Please double-check your code and try again.",
                "receipt_code": receipt_code,
            },
            status=404,
        )

    return render(
        request,
        "submissions/status_result.html",
        {"submission": submission},
    )


def privacy_policy(request: HttpRequest) -> HttpResponse:
    """Privacy Policy page."""
    return render(request, "submissions/privacy.html")


def terms_of_service(request: HttpRequest) -> HttpResponse:
    """Terms of Service page."""
    return render(request, "submissions/terms.html")


def security_transparency(request: HttpRequest) -> HttpResponse:
    """Security & Transparency page."""
    return render(request, "submissions/security.html")


def how_it_works(request: HttpRequest) -> HttpResponse:
    """Marketing: How it works page."""
    return render(request, "submissions/how_it_works.html")


def pricing(request: HttpRequest) -> HttpResponse:
    """Marketing: Pricing page."""
    return render(request, "submissions/pricing.html")


@require_http_methods(["GET", "POST"])
def contact(request: HttpRequest) -> HttpResponse:
    """Contact / Book demo page."""
    if request.method == "GET":
        return render(request, "submissions/contact.html")

    company_name = sanitize_input(request.POST.get("company_name") or "", max_length=120)
    email = sanitize_input(request.POST.get("email") or "", max_length=254)
    message = sanitize_input(request.POST.get("message") or "", max_length=4000)

    errors = []
    if not company_name or len(company_name) < 2:
        errors.append("Company name must be at least 2 characters.")
    if not email or "@" not in email:
        errors.append("Please enter a valid email address.")
    if not message or len(message) < 10:
        errors.append("Message must be at least 10 characters.")

    if errors:
        return render(
            request,
            "submissions/contact.html",
            {"error": " ".join(errors), "company_name": html.unescape(company_name), "email": html.unescape(email), "message": html.unescape(message)},
            status=400,
        )

    # Send contact form email to sales@kyrex.co (non-blocking to prevent worker timeout)
    contact_email = os.environ.get("CONTACT_EMAIL", "sales@kyrex.co")
    import logging
    import traceback
    import sys
    import threading
    from datetime import datetime
    
    logger = logging.getLogger(__name__)
    
    # Print immediately when form is submitted - use multiple methods to ensure visibility
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Force output to stdout/stderr with flush to ensure Railway captures it
    try:
        print("\n" + "=" * 80, file=sys.stdout, flush=True)
        print(f"[{timestamp}] *** CONTACT FORM SUBMITTED ***", file=sys.stdout, flush=True)
        print(f"Company: {html.unescape(company_name)}", file=sys.stdout, flush=True)
        print(f"Email: {html.unescape(email)}", file=sys.stdout, flush=True)
        print(f"Message length: {len(message)} characters", file=sys.stdout, flush=True)
        print("=" * 80 + "\n", file=sys.stdout, flush=True)
        
        # Also print to stderr as backup
        print(f"[{timestamp}] CONTACT FORM: Form submitted - {html.unescape(company_name)}", file=sys.stderr, flush=True)
        
        # Also log to logger
        logger.info(f"CONTACT FORM SUBMITTED: Company={html.unescape(company_name)}, Email={html.unescape(email)}")
    except Exception as log_error:
        # Even if logging fails, don't break the form
        print(f"Error in logging: {log_error}", file=sys.stderr, flush=True)
    
    def send_email_async():
        """Send email in background thread to prevent blocking."""
        try:
            # Print to stdout/stderr for immediate visibility in Railway logs
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("\n" + "=" * 80, file=sys.stdout, flush=True)
            print(f"[{timestamp}] *** CONTACT FORM: Starting email send process ***", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: Recipient: {contact_email}", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: Email backend: {settings.EMAIL_BACKEND}", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: Email host: {getattr(settings, 'EMAIL_HOST', 'Not set')}", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: Email port: {getattr(settings, 'EMAIL_PORT', 'Not set')}", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: Email use TLS: {getattr(settings, 'EMAIL_USE_TLS', 'Not set')}", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: Email user: {getattr(settings, 'EMAIL_HOST_USER', 'Not set')}", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: Email password set: {'Yes' if getattr(settings, 'EMAIL_HOST_PASSWORD', '') else 'No'}", file=sys.stdout, flush=True)
            print(f"CONTACT FORM: From email: {settings.DEFAULT_FROM_EMAIL}", file=sys.stdout, flush=True)
            print("=" * 80 + "\n", file=sys.stdout, flush=True)
            
            # Also log to logger
            logger.info(f"Attempting to send contact form email to {contact_email}")
            logger.info(f"Email backend: {settings.EMAIL_BACKEND}")
            logger.info(f"Email host: {getattr(settings, 'EMAIL_HOST', 'Not set')}")
            logger.info(f"From email: {settings.DEFAULT_FROM_EMAIL}")
            
            # Try to send email and catch any exceptions
            try:
                result = send_mail(
                    subject=f"Contact Form Submission from {html.unescape(company_name)}",
                    message=(
                        f"New contact form submission:\n\n"
                        f"Company name: {html.unescape(company_name)}\n"
                        f"Email: {html.unescape(email)}\n\n"
                        f"Message:\n{html.unescape(message)}\n\n"
                        f"---\n"
                        f"This message was sent from the contact form on {request.build_absolute_uri('/contact/')}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[contact_email],
                    fail_silently=False,  # Set to False to catch errors
                )
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("\n" + "=" * 80, file=sys.stdout, flush=True)
                print(f"[{timestamp}] *** CONTACT FORM: Email send result: {result} ***", file=sys.stdout, flush=True)
                print(f"CONTACT FORM: From: {settings.DEFAULT_FROM_EMAIL}", file=sys.stdout, flush=True)
                print(f"CONTACT FORM: To: {contact_email}", file=sys.stdout, flush=True)
                print("=" * 80 + "\n", file=sys.stdout, flush=True)
                logger.info(f"Contact form email sent successfully to {contact_email}, result: {result}")
            except Exception as send_error:
                # Catch SMTP errors that fail_silently=False would raise
                error_msg = f"SMTP Error sending email: {type(send_error).__name__}: {send_error}"
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("\n" + "=" * 80, file=sys.stderr, flush=True)
                print(f"[{timestamp}] *** CONTACT FORM: SMTP ERROR ***", file=sys.stderr, flush=True)
                print(error_msg, file=sys.stderr, flush=True)
                print(traceback.format_exc(), file=sys.stderr, flush=True)
                print("=" * 80 + "\n", file=sys.stderr, flush=True)
                logger.error(error_msg)
                logger.error(traceback.format_exc())
                raise  # Re-raise to be caught by outer exception handler
        except Exception as e:
            # Log email sending errors but don't fail the form submission
            error_msg = f"Error sending contact form email to {contact_email}: {type(e).__name__}: {e}"
            traceback_str = traceback.format_exc()
            
            # Print to stderr for immediate visibility in Railway logs
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("\n" + "=" * 80, file=sys.stderr, flush=True)
            print(f"[{timestamp}] *** CONTACT FORM ERROR ***", file=sys.stderr, flush=True)
            print(f"CONTACT FORM ERROR: {error_msg}", file=sys.stderr, flush=True)
            print(traceback_str, file=sys.stderr, flush=True)
            print("=" * 80 + "\n", file=sys.stderr, flush=True)
            
            # Also log to logger
            logger.error(error_msg)
            logger.error(traceback_str)
    
    # Send email in background thread to prevent worker timeout
    email_thread = threading.Thread(target=send_email_async, daemon=True)
    email_thread.start()

    return render(request, "submissions/contact.html", {"success": True})


@require_http_methods(["GET", "POST"])
def hr_register(request: HttpRequest) -> HttpResponse:
    """
    Public HR registration page.

    Collects company name + HR email + website, creates a staff user + HrAccessCode,
    generates a unique access code, and emails the code to the HR email.
    """
    if request.method == "GET":
        return render(request, "submissions/hr_register.html")

    company_name = sanitize_input(request.POST.get("company_name") or "", max_length=150)
    email = sanitize_input(request.POST.get("email") or "", max_length=254)
    website = sanitize_input(request.POST.get("website") or "", max_length=200)

    # Basic rate limit (separate from employee submit)
    ip_address = request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip() or request.META.get("REMOTE_ADDR", "unknown")
    cache_key = f"rate_limit_hr_register_{ip_address}"
    count = cache.get(cache_key, 0)
    if count >= 5:
        return render(
            request,
            "submissions/hr_register.html",
            {
                "error": "Too many registration attempts. Please try again later.",
                "company_name": html.unescape(company_name),
                "email": html.unescape(email),
                "website": html.unescape(website),
            },
            status=429,
        )
    cache.set(cache_key, count + 1, 3600)

    errors = []
    if not company_name or len(company_name) < 2:
        errors.append("Company name must be at least 2 characters.")
    if not email or "@" not in email:
        errors.append("Please enter a valid email address.")
    if website and not (website.startswith("http://") or website.startswith("https://")):
        errors.append("Website must start with http:// or https:// (or leave it empty).")

    if errors:
        return render(
            request,
            "submissions/hr_register.html",
            {
                "error": " ".join(errors),
                "company_name": html.unescape(company_name),
                "email": html.unescape(email),
                "website": html.unescape(website),
            },
            status=400,
        )

    # Create staff user + HrAccessCode
    from django.contrib.auth.models import User
    from .models import HrAccessCode
    import secrets

    base_username = (email.split("@")[0] or "hr").lower()
    base_username = re.sub(r"[^a-z0-9_]", "_", base_username)[:20] or "hr"

    # Ensure unique username
    username = base_username
    for _ in range(10):
        if not User.objects.filter(username=username).exists():
            break
        username = f"{base_username}_{secrets.randbelow(9999)}"
    else:
        username = f"hr_{secrets.token_hex(4)}"

    # If user already exists, re-use it; otherwise create a new one
    user, created = User.objects.get_or_create(
        email=html.unescape(email),
        defaults={"username": username},
    )

    # Make sure it's staff so it can have an access code
    if not user.is_staff:
        user.is_staff = True
    if not user.username:
        user.username = username
    if created:
        user.set_unusable_password()
    user.save()

    hr_access = HrAccessCode.get_or_create_for_user(user)
    hr_access.notification_email = html.unescape(email)
    hr_access.company_name = html.unescape(company_name)
    hr_access.company_website = html.unescape(website)
    hr_access.is_active = True
    hr_access.save()

    # Email the access code
    try:
        send_mail(
            subject="Your KYREX HR access code",
            message=(
                f"Hi {hr_access.company_name},\n\n"
                f"Your HR access code is: {hr_access.access_code}\n\n"
                f"Employees can submit feedback using this code at:\n"
                f"{request.build_absolute_uri('/submit/')}\n\n"
                f"If you did not request this, you can ignore this email.\n"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[html.unescape(email)],
            fail_silently=False,
        )
    except Exception as e:
        # Don't lose the created code; show a helpful error
        return render(
            request,
            "submissions/hr_register.html",
            {
                "error": f"Account created, but we could not send the email. Please contact support. ({type(e).__name__})",
                "company_name": hr_access.company_name,
                "email": hr_access.notification_email,
                "website": hr_access.company_website,
            },
            status=500,
        )

    return render(
        request,
        "submissions/hr_register.html",
        {
            "success": True,
            "company_name": hr_access.company_name,
            "email": hr_access.notification_email,
            "website": hr_access.company_website,
        },
    )
