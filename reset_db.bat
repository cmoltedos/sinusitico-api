del publish\migrations\0*.py
del db.sqlite3
python manage.py makemigrations
python manage.py migrate