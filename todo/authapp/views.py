from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from authapp.models import TodoUser
from authapp.serializers import TodoUserModelSerializer


class TodoUserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
