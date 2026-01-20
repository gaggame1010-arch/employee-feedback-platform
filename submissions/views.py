import html
import re

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

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

    # Validate access code
    access_code = (request.POST.get("access_code") or "").strip()
    if access_code != settings.COMPANY_ACCESS_CODE:
        return render(
            request,
            "submissions/submit.html",
            {
                "error": "Invalid company access code. Please check and try again.",
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
        s = Submission.create_with_unique_receipt(
            type=submission_type,
            title=html.unescape(title),  # Store unescaped in DB
            body=html.unescape(body),  # Store unescaped in DB
        )
    except Exception as e:
        return render(
            request,
            "submissions/submit.html",
            {
                "error": "An error occurred while submitting. Please try again.",
                "access_code": access_code,
            },
            status=500,
        )

    # Notify HR (dev default prints email to console)
    if settings.HR_NOTIFY_EMAILS:
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
                recipient_list=settings.HR_NOTIFY_EMAILS,
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
