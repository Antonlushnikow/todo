from django.contrib.auth.models import AbstractUser
from django.db import models


class TodoUser(AbstractUser):
    email = models.EmailField(
        verbose_name='адрес электронной почты',
        unique=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
