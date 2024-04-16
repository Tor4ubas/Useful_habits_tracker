import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """ Создание суперпользователя """

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='alex1029@yandex.ru',
            first_name='Admin',
            last_name='Adminov',
            chat_id=os.getenv("CHAT_ID_ADMIN"),
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('123qwe456rty')
        user.save()
