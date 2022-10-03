from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from authapp.models import TodoUser
from authapp.serializers import TodoUserModelSerializer


class TodoUserModelViewSet(ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer
