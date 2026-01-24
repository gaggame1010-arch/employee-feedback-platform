"""
Rate limiting middleware for anonymous submissions.
"""
import os
from django.core.cache import cache
from django.http import HttpResponse
from django.utils import timezone


class RateLimitMiddleware:
    """
    Rate limit anonymous submissions to prevent abuse.
    Limits: 5 submissions per IP per hour.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Block password change for HR staff (non-superuser)
        if request.path.startswith("/admin/password_change/"):
            user = getattr(request, "user", None)
            if user and user.is_authenticated and user.is_staff and not user.is_superuser:
                return HttpResponse("Password changes are disabled for this account.", status=403)
        # Only rate limit POST requests to submit endpoint
        if request.method == "POST" and request.path in ("/submit/", "/hr/register/"):
            ip_address = self.get_client_ip(request)
            # Separate buckets per endpoint
            bucket = "submit" if request.path == "/submit/" else "hr_register"
            cache_key = f"rate_limit_{bucket}_{ip_address}"
            
            # Get current count
            count = cache.get(cache_key, 0)
            
            # Rate limit: 10 submissions per hour (configurable via environment variable)
            if request.path == "/hr/register/":
                max_submissions = int(os.environ.get("RATE_LIMIT_HR_REGISTER_MAX", "10"))  # Increased to 10 per hour
                rate_limit_window = int(os.environ.get("RATE_LIMIT_HR_REGISTER_WINDOW_SECONDS", "3600"))
            else:
                max_submissions = int(os.environ.get("RATE_LIMIT_MAX_SUBMISSIONS", "10"))
                rate_limit_window = int(os.environ.get("RATE_LIMIT_WINDOW_SECONDS", "3600"))  # 1 hour default
            
            if count >= max_submissions:
                # Return a more helpful error page for HR registration
                if request.path == "/hr/register/":
                    from django.shortcuts import render
                    return render(
                        request,
                        "submissions/hr_register.html",
                        {
                            "error": "Too many registration attempts. Please wait an hour and try again, or contact support if you need immediate assistance.",
                        },
                        status=429,
                    )
                return HttpResponse(
                    "Too many requests. Please try again later.",
                    status=429,
                )
            
            # Increment counter (expires in rate_limit_window seconds)
            cache.set(cache_key, count + 1, rate_limit_window)
        
        response = self.get_response(request)
        return response

    @staticmethod
    def get_client_ip(request):
        """Extract client IP address from request."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR", "unknown")
        return ip
