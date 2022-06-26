web:gunicorn DAWAYEE_USER_API.wsgi
release:python manage.py makemigrations --noinput
release:python manage.py collectstatic --noinput
release:python manage.py migrate --noinput