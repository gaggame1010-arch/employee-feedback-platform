"""
Management command to create admin user if it doesn't exist.
Can be run non-interactively with environment variables.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Create admin user from environment variables (non-interactive)'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'hr_admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'sales@kyrex.co')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write(
                self.style.ERROR('DJANGO_SUPERUSER_PASSWORD environment variable is required')
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" already exists. Skipping creation.')
            )
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created superuser "{username}"')
        )
