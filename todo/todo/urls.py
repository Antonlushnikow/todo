from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authapp.views import TodoUserModelViewSet
from mainapp.views import ProjectModelViewSet, TodoModelViewSet

router = DefaultRouter()
router.register('users', TodoUserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
