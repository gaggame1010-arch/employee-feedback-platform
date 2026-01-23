# Railway will run 'release' command before starting the web service
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py create_admin || echo "Release command completed with warnings"
web: gunicorn anonplatform.wsgi:application
