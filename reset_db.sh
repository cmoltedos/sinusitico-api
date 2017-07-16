#!/bin/bash
rm publish/migrations/0*.py
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate