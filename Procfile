release: python manage.py migrate
web: gunicorn anonplatform.wsgi --bind 0.0.0.0:$PORT --log-file -
