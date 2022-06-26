web:gunicorn DAWAYEE_USER_API.wsgi --log-file -
web: python manage.py runserver 0.0.0.0:5000
release:python manage.py makemigrations --noinput
release:python manage.py collectstatic --noinput
release:python manage.py migrate --noinput