#!/bin/bash
# Script to ensure migrations run before starting the server
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating admin user (if needed)..."
python manage.py create_admin || true

echo "Starting server..."
exec "$@"
