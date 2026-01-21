release: python manage.py migrate --noinput; python manage.py collectstatic --noinput
web: python -c "import os; port = os.environ.get('PORT', '8000'); exec('import subprocess; subprocess.run([\"gunicorn\", \"anonplatform.wsgi:application\", \"--bind\", f\"0.0.0.0:{port}\"])')"
