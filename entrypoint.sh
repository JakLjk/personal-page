#!/bin/sh

set -e 

echo "Running collectstatic..."
poetry run python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec poetry run gunicorn personal_blog.wsgi:application --bind 0.0.0.0:8000