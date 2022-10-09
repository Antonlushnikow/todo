from django.db import models

from authapp.models import TodoUser


class Project(models.Model):
    name = models.CharField(
        verbose_name='название проекта',
        max_length=64,
        blank=False,
    )
    repo_link = models.CharField(
        verbose_name='ссылка на репозиторий',
        max_length=512,
        blank=True,
    )
    users = models.ManyToManyField(TodoUser)

    def __str__(self):
        return self.name


class Todo(models.Model):
    user = models.ForeignKey(
        TodoUser,
        verbose_name='создатель',
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(
        Project,
        verbose_name='проект',
        on_delete=models.CASCADE,
    )
    body = models.TextField(verbose_name='текст заметки',)
    created_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True,
    )
    is_active = models.BooleanField(
        verbose_name='активно',
        default=True,
    )
    is_closed = models.BooleanField(
        verbose_name='закрыто',
        default=False,
    )
