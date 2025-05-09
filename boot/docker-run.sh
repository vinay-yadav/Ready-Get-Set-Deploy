#!/bin/bash

source /opt/venv/bin/activate
cd /code

python manage.py sendtestemail --admins
python manage.py migrate --no-input
python manage.py auto_admin

export RUNTIME_PORT = 8080

# Add static files to container itself on runtime
#python manage.py collectstatic --no-input

gunicorn deploy_django.wsgi:application --bind 0.0.0.0:$RUNTIME_PORT