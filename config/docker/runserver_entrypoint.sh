#!/bin/sh

set -e

python manage.py makemigrations

gunicorn --workers=2 \
--thread=4 \
--worker-tmp-dir /dev/shm \
--bind=0.0.0.0:8000 \
--log-level=info \
--access-logfile=- \
--error-logfile =- \
sample.wsgi
