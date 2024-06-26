Проект "Трекер полезных привычек"

Данный проект представляет собой веб-приложение для отслеживания полезных привычек. Вдохновлен книгой "Атомные привычки" Джеймса Клира, он помогает пользователям формировать новые полезные привычки и избавляться от старых плохих привычек.

О проекте

Проект состоит из двух основных частей: бэкенд-части на основе Django Rest Framework. Бэкенд обеспечивает API для работы с привычками и пользователями, а также интеграцию с мессенджером Telegram для напоминаний.

Возможности

    Регистрация и авторизация пользователей
    Создание, чтение, обновление и удаление привычек
    Просмотр списка привычек пользователя с пагинацией
    Просмотр списка общедоступных привычек
    Интеграция с мессенджером Telegram для отправки уведомлений о привычках

Технологии

    python = 3.10
    django = 5.0.4
    psycopg2-binary = 2.9.9
    pillow = 9.0.1
    ipython = 8.12.13
    djangorestframework = 3.14.0
    djangorestframework-simplejwt = 5.3.1
    drf-yasg = 1.21.7
    requests = 2.31.0
    celery = 5.3.6
    python-dotenv = 1.0.1
    redis = 5.0.3
    flake8 = 7.0.0
    django-celery-beat = 2.6.0
    pytest-cov = 5.0.0

Запуск проекта

    Склонируйте этот репозиторий к себе

    В проекте используется Poetry, при развертывании локально, он подтянет зависимости автоматически 

    Создайте файл .env в корневой директории и заполните необходимые переменные окружения:
        BASE_NAME=имя_базы_данных
        BASE_USER=пользователь_базы_данных
        TELEGRAM_TOKEN=токен_Telegram_бота
        

    Примените миграции:
        python3 manage.py migrate

    Запустите сервер:
        python3 manage.py runserver

    Запустите Celery для обработки отложенных задач:
        celery -A config worker --pool=solo -l INFO
        celery -A config beat -l info -S django

    Используйте команду csu для создания тестового суперпользователя
        python manage.py csu

    Подготовьте телеграм бота для отправки данных
        Запустите бота командой /start

Для запуска проекта через Docker необходимо:

    Выполнить команды:

    docker compose build - сборка образа
    docker compose up - запуск контейнера

Документация API

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/docs/
