# Railway will run 'release' command before starting the web service
# This ensures migrations run automatically on each deployment
release: python manage.py migrate --noinput; python manage.py collectstatic --noinput; python manage.py create_admin || true
web: gunicorn anonplatform.wsgi:application --timeout 120 --workers 2
