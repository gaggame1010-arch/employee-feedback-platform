from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from django.template.response import TemplateResponse
from django.urls import path

from .models import HrResponse, Submission

admin.site.site_header = "HR Dashboard"
admin.site.site_title = "HR Dashboard"
admin.site.index_title = "Submissions"

# Note: Django admin already requires staff status by default

# Override admin index to add statistics
original_index = admin.site.index

def custom_index(request, extra_context=None):
    """Custom admin index with statistics."""
    extra_context = extra_context or {}
    
    # Get statistics
    total_submissions = Submission.objects.count()
    new_submissions = Submission.objects.filter(status=Submission.Status.NEW).count()
    in_review = Submission.objects.filter(status=Submission.Status.IN_REVIEW).count()
    responded = Submission.objects.filter(status=Submission.Status.RESPONDED).count()
    closed = Submission.objects.filter(status=Submission.Status.CLOSED).count()
    
    # Count by type
    issues = Submission.objects.filter(type=Submission.SubmissionType.ISSUE).count()
    concerns = Submission.objects.filter(type=Submission.SubmissionType.CONCERN).count()
    questions = Submission.objects.filter(type=Submission.SubmissionType.QUESTION).count()
    suggestions = Submission.objects.filter(type=Submission.SubmissionType.SUGGESTION).count()
    
    # Recent submissions
    recent_submissions = Submission.objects.select_related("hr_response").order_by("-created_at")[:5]
    
    extra_context.update({
        "total_submissions": total_submissions,
        "new_submissions": new_submissions,
        "in_review": in_review,
        "responded": responded,
        "closed": closed,
        "issues": issues,
        "concerns": concerns,
        "questions": questions,
        "suggestions": suggestions,
        "recent_submissions": recent_submissions,
    })
    
    return original_index(request, extra_context)

admin.site.index = custom_index

# Unregister default User and Group to customize them
admin.site.unregister(User)
admin.site.unregister(Group)


# Custom User Admin for Authentication and Authorization
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "full_name", "is_active_badge", "is_staff_badge", "is_superuser_badge", "date_joined", "last_login")
    list_filter = ("is_staff", "is_superuser", "is_active", "date_joined", "groups")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-date_joined",)
    list_per_page = 25
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    
    readonly_fields = ("last_login", "date_joined")
    
    def full_name(self, obj):
        """Display full name or username if no name."""
        if obj.first_name or obj.last_name:
            return f"{obj.first_name} {obj.last_name}".strip()
        return format_html('<span style="color: #6b7280;">—</span>')
    full_name.short_description = "Name"
    
    def is_active_badge(self, obj):
        """Display active status with badge."""
        if obj.is_active:
            return format_html(
                '<span style="display: inline-block; padding: 4px 10px; border-radius: 12px; background: rgba(34, 197, 94, 0.2); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.4); font-size: 11px; font-weight: 700;">Active</span>'
            )
        return format_html(
            '<span style="display: inline-block; padding: 4px 10px; border-radius: 12px; background: rgba(107, 114, 128, 0.2); color: #6b7280; border: 1px solid rgba(107, 114, 128, 0.4); font-size: 11px; font-weight: 700;">Inactive</span>'
        )
    is_active_badge.short_description = "Status"
    is_active_badge.admin_order_field = "is_active"
    
    def is_staff_badge(self, obj):
        """Display staff status with badge."""
        if obj.is_staff:
            return format_html(
                '<span style="display: inline-block; padding: 4px 10px; border-radius: 12px; background: rgba(44, 102, 255, 0.2); color: #2c66ff; border: 1px solid rgba(44, 102, 255, 0.4); font-size: 11px; font-weight: 700;">Staff</span>'
            )
        return format_html('<span style="color: #6b7280;">—</span>')
    is_staff_badge.short_description = "Staff"
    is_staff_badge.admin_order_field = "is_staff"
    is_staff_badge.boolean = True
    
    def is_superuser_badge(self, obj):
        """Display superuser status with badge."""
        if obj.is_superuser:
            return format_html(
                '<span style="display: inline-block; padding: 4px 10px; border-radius: 12px; background: rgba(124, 58, 237, 0.2); color: #7c3aed; border: 1px solid rgba(124, 58, 237, 0.4); font-size: 11px; font-weight: 700;">Admin</span>'
            )
        return format_html('<span style="color: #6b7280;">—</span>')
    is_superuser_badge.short_description = "Admin"
    is_superuser_badge.admin_order_field = "is_superuser"
    is_superuser_badge.boolean = True


# Custom Group Admin
@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "user_count")
    search_fields = ("name",)
    filter_horizontal = ("permissions",)
    
    def user_count(self, obj):
        """Display number of users in the group."""
        count = obj.user_set.count()
        return format_html(
            '<span style="color: #2c66ff; font-weight: 700;">{}</span>',
            count
        )
    user_count.short_description = "Users"


class HrResponseInline(admin.StackedInline):
    model = HrResponse
    extra = 0  # Don't show extra empty forms if response exists
    max_num = 1
    min_num = 0
    fields = ("body",)
    verbose_name = "HR Response"
    verbose_name_plural = "HR Responses"
    can_delete = True
    
    def get_readonly_fields(self, request, obj=None):
        """Make body editable."""
        return []
    
    def get_extra(self, request, obj=None, **kwargs):
        """Show one empty form only if no response exists."""
        if obj and hasattr(obj, 'hr_response') and obj.hr_response:
            return 0
        return 1


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("receipt_code_display", "type_badge", "status_badge", "title_truncated", "submitted_time", "has_response", "updated_at")
    list_filter = ("type", "status", "created_at", "updated_at")
    search_fields = ("receipt_code", "title", "body")
    readonly_fields = ("receipt_code", "created_at", "updated_at", "submission_preview")
    inlines = [HrResponseInline]
    list_per_page = 25
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    list_select_related = ("hr_response",)
    actions = ["mark_as_in_review", "mark_as_responded", "mark_as_closed"]
    
    fieldsets = (
        ("Submission Details", {
            "fields": ("receipt_code", "type", "status", "title", "body", "submission_preview"),
            "description": "View the employee's submission below. Scroll down to the 'HR Responses' section to add your reply."
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )
    
    def mark_as_in_review(self, request, queryset):
        """Mark selected submissions as in review."""
        queryset.update(status=Submission.Status.IN_REVIEW)
        self.message_user(request, f"{queryset.count()} submission(s) marked as In Review.")
    mark_as_in_review.short_description = "Mark selected as In Review"
    
    def mark_as_responded(self, request, queryset):
        """Mark selected submissions as responded."""
        queryset.update(status=Submission.Status.RESPONDED)
        self.message_user(request, f"{queryset.count()} submission(s) marked as Responded.")
    mark_as_responded.short_description = "Mark selected as Responded"
    
    def mark_as_closed(self, request, queryset):
        """Mark selected submissions as closed."""
        queryset.update(status=Submission.Status.CLOSED)
        self.message_user(request, f"{queryset.count()} submission(s) marked as Closed.")
    mark_as_closed.short_description = "Mark selected as Closed"
    
    def save_model(self, request, obj, form, change):
        """Auto-update status when HR responds."""
        super().save_model(request, obj, form, change)
        
        # If HR response exists and status is not RESPONDED, update it
        if hasattr(obj, 'hr_response') and obj.hr_response and obj.status != Submission.Status.RESPONDED:
            obj.status = Submission.Status.RESPONDED
            obj.save(update_fields=['status'])
    
    def save_formset(self, request, form, formset, change):
        """Handle HR response inline saving."""
        if formset.model == HrResponse:
            # Use Django's standard formset saving
            instances = formset.save(commit=False)
            submission = form.instance
            
            # Save instances
            for instance in instances:
                if instance:
                    instance.save()
                    # Update submission status to RESPONDED when HR adds/updates a response
                    if submission and submission.status != Submission.Status.RESPONDED:
                        submission.status = Submission.Status.RESPONDED
                        submission.save(update_fields=['status'])
            
            # Handle deletions
            for obj in formset.deleted_objects:
                obj.delete()
            
            # Save many-to-many relationships
            formset.save_m2m()
        else:
            # For other formsets, use default behavior
            super().save_formset(request, form, formset, change)

    def receipt_code_display(self, obj):
        """Display receipt code with monospace font and link."""
        if not obj:
            return "—"
        if obj.pk:
            return format_html(
                '<a href="/admin/submissions/submission/{}/change/" style="font-family: ui-monospace, monospace; font-size: 13px; letter-spacing: 0.5px; color: #2c66ff; text-decoration: none; font-weight: 700;">{}</a>',
                obj.pk,
                obj.receipt_code
            )
        return format_html(
            '<span style="font-family: ui-monospace, monospace; font-size: 13px; letter-spacing: 0.5px; color: #2c66ff;">{}</span>',
            obj.receipt_code
        )
    receipt_code_display.short_description = "Receipt Code"
    receipt_code_display.admin_order_field = "receipt_code"

    def type_badge(self, obj):
        """Display type with colored badge."""
        if not obj or not hasattr(obj, 'type'):
            return "—"
        styles = {
            "ISSUE": "background: rgba(239, 68, 68, 0.2); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.4);",
            "CONCERN": "background: rgba(245, 158, 11, 0.2); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.4);",
            "QUESTION": "background: rgba(44, 102, 255, 0.2); color: #2c66ff; border: 1px solid rgba(44, 102, 255, 0.4);",
            "SUGGESTION": "background: rgba(34, 197, 94, 0.2); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.4);",
        }
        style = styles.get(obj.type, "background: rgba(107, 114, 128, 0.2); color: #6b7280; border: 1px solid rgba(107, 114, 128, 0.4);")
        return format_html(
            '<span style="display: inline-block; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; {}">{}</span>',
            style,
            obj.get_type_display()
        )
    type_badge.short_description = "Type"
    type_badge.admin_order_field = "type"

    def status_badge(self, obj):
        """Display status with colored badge."""
        if not obj or not hasattr(obj, 'status'):
            return "—"
        styles = {
            "NEW": "background: rgba(245, 158, 11, 0.2); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.4);",
            "IN_REVIEW": "background: rgba(59, 130, 246, 0.2); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.4);",
            "RESPONDED": "background: rgba(34, 197, 94, 0.2); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.4);",
            "CLOSED": "background: rgba(107, 114, 128, 0.2); color: #6b7280; border: 1px solid rgba(107, 114, 128, 0.4);",
        }
        style = styles.get(obj.status, "background: rgba(107, 114, 128, 0.2); color: #6b7280; border: 1px solid rgba(107, 114, 128, 0.4);")
        return format_html(
            '<span style="display: inline-block; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; {}">{}</span>',
            style,
            obj.get_status_display()
        )
    status_badge.short_description = "Status"
    status_badge.admin_order_field = "status"

    def title_truncated(self, obj):
        """Display truncated title."""
        if not obj or not hasattr(obj, 'title'):
            return "—"
        if len(obj.title) > 50:
            return format_html('<span title="{}">{}...</span>', obj.title, obj.title[:50])
        return obj.title
    title_truncated.short_description = "Title"
    title_truncated.admin_order_field = "title"

    def submitted_time(self, obj):
        """Display submission time in a readable format."""
        try:
            from django.utils import timezone
            from datetime import timedelta
            
            if not obj or not hasattr(obj, 'created_at') or not obj.created_at:
                return "—"
            
            # Convert to local time if timezone aware
            if timezone.is_aware(obj.created_at):
                local_time = timezone.localtime(obj.created_at)
                now = timezone.localtime(timezone.now())
            else:
                local_time = obj.created_at
                from django.utils import timezone as tz
                now = tz.make_naive(tz.now())
            
            # Format: "Jan 20, 2026 at 3:45 PM"
            time_str = local_time.strftime("%b %d, %Y at %I:%M %p")
            
            # Calculate time difference
            diff = now - local_time
            
            # Add relative time (e.g., "2 hours ago")
            if diff.total_seconds() < 60:
                relative = "just now"
            elif diff.total_seconds() < 3600:
                minutes = int(diff.total_seconds() / 60)
                relative = f"{minutes} min{'s' if minutes != 1 else ''} ago"
            elif diff.days == 0:
                hours = int(diff.total_seconds() / 3600)
                relative = f"{hours} hour{'s' if hours != 1 else ''} ago"
            elif diff.days < 7:
                days = diff.days
                relative = f"{days} day{'s' if days != 1 else ''} ago"
            else:
                relative = None
            
            if relative:
                return format_html(
                    '<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 700; color: #e8eefc; font-size: 13px;">{}</span><span style="font-size: 11px; color: rgba(232,238,252,.6);">{}</span></div>',
                    time_str,
                    relative
                )
            return format_html(
                '<span style="font-weight: 700; color: #e8eefc; font-size: 13px;">{}</span>',
                time_str
            )
        except Exception as e:
            # Fallback to simple display if there's any error
            if obj and hasattr(obj, 'created_at') and obj.created_at:
                return str(obj.created_at)
            return "—"
    submitted_time.short_description = "Submitted"
    submitted_time.admin_order_field = "created_at"

    def has_response(self, obj):
        """Display checkmark if HR has responded."""
        try:
            if hasattr(obj, 'hr_response') and obj.hr_response:
                return format_html(
                    '<span style="color: #22c55e; font-weight: 700; font-size: 16px;">✓</span>'
                )
        except Exception:
            pass
        return format_html(
            '<span style="color: #6b7280;">—</span>'
        )
    has_response.short_description = "Response"
    has_response.boolean = True

    def submission_preview(self, obj):
        """Show a formatted preview of the submission."""
        if not obj.pk:
            return "Save to see preview"
        preview = obj.body[:200] + "..." if len(obj.body) > 200 else obj.body
        return format_html(
            '<div style="background: rgba(0,0,0,0.2); padding: 12px; border-radius: 8px; white-space: pre-wrap; font-size: 13px; line-height: 1.6;">{}</div>',
            preview
        )
    submission_preview.short_description = "Preview"

    def has_delete_permission(self, request, obj=None):
        """Only superusers can delete submissions."""
        return request.user.is_superuser

    def get_queryset(self, request):
        """Optimize queryset with select_related."""
        qs = super().get_queryset(request)
        return qs.select_related("hr_response")


@admin.register(HrResponse)
class HrResponseAdmin(admin.ModelAdmin):
    list_display = ("submission_link", "response_preview", "created_at", "updated_at")
    search_fields = ("submission__receipt_code", "submission__title", "body")
    readonly_fields = ("created_at", "updated_at", "response_preview_field")
    list_per_page = 25
    ordering = ("-created_at",)
    
    fieldsets = (
        ("Response Details", {
            "fields": ("submission", "body", "response_preview_field")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    def submission_link(self, obj):
        """Display submission with link."""
        return format_html(
            '<a href="/admin/submissions/submission/{}/change/" style="color: #2c66ff; font-weight: 700;">{}</a>',
            obj.submission.id,
            obj.submission.receipt_code
        )
    submission_link.short_description = "Submission"

    def response_preview(self, obj):
        """Display truncated response."""
        if len(obj.body) > 60:
            return format_html('<span title="{}">{}...</span>', obj.body, obj.body[:60])
        return obj.body
    response_preview.short_description = "Response"

    def response_preview_field(self, obj):
        """Show formatted preview of response."""
        if not obj.pk:
            return "Save to see preview"
        return format_html(
            '<div style="background: rgba(0,0,0,0.2); padding: 12px; border-radius: 8px; white-space: pre-wrap; font-size: 13px; line-height: 1.6;">{}</div>',
            obj.body
        )
    response_preview_field.short_description = "Preview"
