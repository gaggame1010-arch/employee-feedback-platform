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
            try:
                user = UserModel.objects.get(email__iexact=username)
            except UserModel.DoesNotExist:
                return None
        else:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
