web gunicorn DAWAYEE_USER_API.wsgi --timeout 200 --log-file -
# web: python manage.py runserver 0.0.0.0:8000
# web: waitress-serve --port=$PORT DAWAYEE_USER_API.wsgi:application
release:python manage.py makemigrations --noinput
# release:python manage.py collectstatic --noinput
release:python manage.py migrate --noinput
