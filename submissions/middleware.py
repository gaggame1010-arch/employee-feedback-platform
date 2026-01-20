"""
Rate limiting middleware for anonymous submissions.
"""
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
        # Only rate limit POST requests to submit endpoint
        if request.method == "POST" and request.path == "/submit/":
            ip_address = self.get_client_ip(request)
            cache_key = f"rate_limit_submit_{ip_address}"
            
            # Get current count
            count = cache.get(cache_key, 0)
            
            if count >= 5:  # Max 5 submissions per hour
                return HttpResponse(
                    "Too many submissions. Please try again later.",
                    status=429,
                )
            
            # Increment counter (expires in 3600 seconds = 1 hour)
            cache.set(cache_key, count + 1, 3600)
        
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
