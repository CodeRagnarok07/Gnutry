python manage.py dumpdata --exclude=auth --exclude=admin --exclude=sessions  --exclude=contenttypes -o db.json

python manage.py dumpdata -o db.json

python manage.py loaddata db.json