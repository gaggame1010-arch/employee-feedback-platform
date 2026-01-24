from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailOrUsernameModelBackend(ModelBackend):
    """Allow authentication with either email or username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        UserModel = get_user_model()
        user = None

        if "@" in username:
            qs = UserModel.objects.filter(email__iexact=username)
            # Prefer staff users when duplicates exist
            staff_qs = qs.filter(is_staff=True)
            if staff_qs.exists():
                qs = staff_qs
            user = qs.order_by("-is_staff", "-is_superuser", "-last_login", "-id").first()
            if not user:
                return None
        else:
            user = UserModel.objects.filter(username=username).first()
            if not user:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
