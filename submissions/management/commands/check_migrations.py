"""
Management command to check migration status and run migrations if needed.
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Check migration status and run migrations if needed'

    def handle(self, *args, **options):
        # Check if database tables exist
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name LIKE 'submissions_%'
                ORDER BY table_name;
            """)
            tables = [row[0] for row in cursor.fetchall()]
        
        self.stdout.write(self.style.SUCCESS(f'Found {len(tables)} submissions tables:'))
        for table in tables:
            self.stdout.write(f'  - {table}')
        
        # Check if migrations table exists
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'django_migrations';
        """)
        has_migrations_table = cursor.fetchone() is not None
        
        if not has_migrations_table:
            self.stdout.write(self.style.ERROR('django_migrations table does not exist!'))
            self.stdout.write(self.style.WARNING('Running migrations...'))
            call_command('migrate', verbosity=2, interactive=False)
        else:
            # Check pending migrations
            cursor.execute("""
                SELECT app, name 
                FROM django_migrations 
                WHERE app = 'submissions'
                ORDER BY id DESC 
                LIMIT 5;
            """)
            applied_migrations = cursor.fetchall()
            
            self.stdout.write(self.style.SUCCESS(f'\nApplied migrations:'))
            for app, name in applied_migrations:
                self.stdout.write(f'  - {app}.{name}')
            
            # Check for pending migrations
            self.stdout.write(self.style.WARNING('\nChecking for pending migrations...'))
            call_command('migrate', verbosity=2, interactive=False, check=True)
