# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r /app/requirements.txt
#RUN pip install Celery
#RUN pip install django_celery_beat
#RUN pip install django-cors-headers
#RUN pip install psycopg2

# Копируем код приложения в контейнер
COPY . .
