from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User
import secrets

from .utils import generate_receipt_code


class HrAccessCode(models.Model):
    """
    Unique access code for each HR user.
    Employees use this code to submit feedback.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="hr_access_code",
        limit_choices_to={"is_staff": True},  # Only staff users can have access codes
    )
    access_code = models.CharField(max_length=20, unique=True, db_index=True)
    # Stored for display/organization; enforced on registration form
    company_name = models.CharField(max_length=150, blank=True, default="")
    company_website = models.URLField(blank=True, default="")
    notification_email = models.EmailField(
        blank=True,
        help_text="Email address to receive notifications for submissions using this code. If empty, uses user's email."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def get_notification_email(self):
        """Get the email address for notifications."""
        return self.notification_email or self.user.email

    class Meta:
        verbose_name = "HR Access Code"
        verbose_name_plural = "HR Access Codes"

    def __str__(self) -> str:
        return f"{self.user.username} - {self.access_code}"

    @classmethod
    def generate_unique_code(cls) -> str:
        """Generate a unique 6-digit access code."""
        max_attempts = 100
        for _ in range(max_attempts):
            code = ''.join(secrets.choice('0123456789') for _ in range(6))
            if not cls.objects.filter(access_code=code).exists():
                return code
        raise RuntimeError("Failed to generate unique access code after multiple attempts.")

    @classmethod
    def get_or_create_for_user(cls, user: User) -> "HrAccessCode":
        """Get or create access code for a user."""
        if not user.is_staff:
            raise ValueError("Only staff users can have access codes")
        
        # Try to get existing first (this will work even if new columns don't exist)
        try:
            # Use values() to get a dict, avoiding column selection issues
            existing = cls.objects.filter(user=user).first()
            if existing:
                return existing
        except Exception:
            # If query fails due to missing columns, try raw SQL approach
            from django.db import connection
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, access_code, notification_email, is_active FROM submissions_hraccesscode WHERE user_id = %s",
                        [user.id]
                    )
                    row = cursor.fetchone()
                    if row:
                        # Reconstruct object (minimal)
                        obj = cls(id=row[0], user=user, access_code=row[1], is_active=row[3])
                        obj.notification_email = row[2] if row[2] else ""
                        return obj
            except Exception:
                pass  # Fall through to create new
        
        # Create new access code
        # Use minimal fields to avoid column issues
        new_code = cls(
            user=user,
            access_code=cls.generate_unique_code(),
            is_active=True
        )
        # Only set notification_email if we can (avoid AttributeError if column doesn't exist)
        try:
            new_code.notification_email = user.email
        except (AttributeError, Exception):
            pass
        new_code.save()
        return new_code


class Submission(models.Model):
    class SubmissionType(models.TextChoices):
        ISSUE = "ISSUE", "Issue"
        CONCERN = "CONCERN", "Concern"
        QUESTION = "QUESTION", "Question"
        SUGGESTION = "SUGGESTION", "Suggestion"

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        IN_REVIEW = "IN_REVIEW", "In review"
        RESPONDED = "RESPONDED", "Responded"
        CLOSED = "CLOSED", "Closed"

    type = models.CharField(max_length=20, choices=SubmissionType.choices)
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    receipt_code = models.CharField(max_length=20, unique=True, db_index=True)
    hr_access_code = models.ForeignKey(
        HrAccessCode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="submissions",
        help_text="The HR access code used to submit this feedback"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.receipt_code} ({self.type})"

    @classmethod
    def create_with_unique_receipt(cls, **kwargs) -> "Submission":
        """
        Create a submission with a digits-only receipt code, retrying on collision.
        """
        max_attempts = 10
        for _ in range(max_attempts):
            try:
                return cls.objects.create(receipt_code=generate_receipt_code(), **kwargs)
            except IntegrityError:
                continue
        raise RuntimeError("Failed to generate unique receipt code after multiple attempts.")


class HrResponse(models.Model):
    submission = models.OneToOneField(
        Submission,
        on_delete=models.CASCADE,
        related_name="hr_response",
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Response for {self.submission.receipt_code}"
