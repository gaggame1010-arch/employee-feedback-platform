"""
WSGI config for anonplatform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anonplatform.settings')

# Run migrations automatically on startup if needed (fallback if release command doesn't run)
# This ensures migrations run even if Railway's release phase doesn't execute
try:
    from django.core.management import execute_from_command_line
    from django.db import connection
    
    # Check if migrations table exists (indicates migrations have run)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'django_migrations';
        """)
        migrations_table_exists = cursor.fetchone() is not None
        
        # Check if submissions_submission table exists
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'submissions_submission';
        """)
        submissions_table_exists = cursor.fetchone() is not None
        
        # If migrations table exists but submissions table doesn't, migrations need to run
        # If migrations table doesn't exist, definitely need to run migrations
        if not migrations_table_exists or not submissions_table_exists:
            print("Migrations not detected. Running migrations automatically...", file=sys.stderr)
            execute_from_command_line(['manage.py', 'migrate', '--noinput'])
            print("Migrations completed.", file=sys.stderr)
except Exception as e:
    # Don't fail startup if migration check fails (might be database connection issue)
    print(f"Warning: Could not check/run migrations on startup: {e}", file=sys.stderr)
    print("Migrations should be run manually if needed.", file=sys.stderr)

application = get_wsgi_application()
