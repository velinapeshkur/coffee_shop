#!/bin/sh

echo "Make migrations";
python manage.py makemigrations
echo "Migrate";
python manage.py migrate
echo "Create superuser";
python manage.py createsuperuser --email=admin@admin.com --noinput
echo "Run server";
python manage.py runserver 0.0.0.0:8000
