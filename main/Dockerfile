FROM python:3.12-slim

WORKDIR /app
COPY . /app/
COPY .env.docker /app/.env

RUN pip install -r requirements/prod.txt

CMD python manage.py migrate --settings=main.settings.prod \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@admin.ru').exists() or User.objects.create_superuser('admin@admin.ru','admin')" --settings=main.settings.prod \
    && python manage.py collectstatic --no-input \
    && gunicorn main.wsgi:application -b 0.0.0.0:8000