from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from authapp.models import TodoUser
from authapp.serializers import TodoUserModelSerializer


# Простой вариант с ViewSet
# class TodoUserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin, viewsets.GenericViewSet):
#     queryset = TodoUser.objects.all()
#     serializer_class = TodoUserModelSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class TodoUserListAPIView(APIView):
    """
    Для разнообразия использовал APIView, хотя с миксинами гораздо проще
    """
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        """
        Просмотр списка пользователей
        """
        users = TodoUser.objects.all()
        serializer = TodoUserModelSerializer(users, many=True)
        return Response(serializer.data)


class TodoUserDetailAPIView(APIView):
    """
    Для разнообразия использовал APIView, хотя с миксинами гораздо проще
    """
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @staticmethod
    def get_object(pk):
        return get_object_or_404(TodoUser, pk=pk)

    def get(self, request, pk, format=None):
        """
        Просмотр пользователя
        """
        user = self.get_object(pk)
        serializer = TodoUserModelSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Изменение пользователя
        """
        user = self.get_object(pk)
        serializer = TodoUserModelSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """
        Изменение части пользователя
        """
        user = self.get_object(pk)
        serializer = TodoUserModelSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
