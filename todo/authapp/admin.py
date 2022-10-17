from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authapp.models import TodoUser

admin.site.register(TodoUser, UserAdmin)
