#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --no-input --settings=backend.settings.production
python manage.py migrate --settings=backend.settings.production