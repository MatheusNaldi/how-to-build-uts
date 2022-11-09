#!/bin/sh

pip install -r /usr/src/app/requirements.txt
pip install -r /usr/src/app/requirements.dev.txt
python manage.py collectstatic --noinput

exec "$@"

