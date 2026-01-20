from django.db import models
from django.db import IntegrityError

from .utils import generate_receipt_code

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
