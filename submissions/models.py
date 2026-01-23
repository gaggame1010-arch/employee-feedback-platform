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
        
        # Try to get or create, handling case where company_name column doesn't exist yet
        try:
            access_code, created = cls.objects.get_or_create(
                user=user,
                defaults={"access_code": cls.generate_unique_code()}
            )
        except Exception as e:
            # If it's a missing column error, try with only() to exclude new fields
            error_str = str(e)
            if "company_name" in error_str or "does not exist" in error_str:
                # Migration hasn't run - use only() to select existing fields
                try:
                    existing = cls.objects.only('id', 'user_id', 'access_code', 'notification_email', 'created_at', 'updated_at', 'is_active').get(user=user)
                    return existing
                except cls.DoesNotExist:
                    # Create new one - but we can't use get_or_create with only()
                    # So we'll create it with minimal fields
                    new_code = cls(
                        user=user,
                        access_code=cls.generate_unique_code(),
                        is_active=True
                    )
                    new_code.save()
                    return new_code
            # Re-raise other errors
            raise
        
        return access_code


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
