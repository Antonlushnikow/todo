from rest_framework.serializers import ModelSerializer

from authapp.models import TodoUser


class TodoUserModelSerializer(ModelSerializer):
    class Meta:
        model = TodoUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        ordering = ['id']
