release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py create_admin || true
web: gunicorn anonplatform.wsgi:application
