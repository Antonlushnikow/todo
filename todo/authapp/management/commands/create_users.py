import json
import os

from django.core.management import BaseCommand

from authapp.models import TodoUser


JSON_PATH = 'authapp\\jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        TodoUser.objects.all().delete()
        users = load_from_json('users')
        for user in users:
            new_category = TodoUser(**user)
            new_category.save()

        super_user = TodoUser.objects.create_superuser('admin', 'admin@admin.ru', '123')
