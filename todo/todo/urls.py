from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authapp.views import TodoUserListAPIView, TodoUserDetailAPIView
from mainapp.views import ProjectModelViewSet, TodoModelViewSet

router = DefaultRouter()
# router.register('users', TodoUserCustomViewSet, basename='user')
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', TodoUserListAPIView.as_view()),
    path('api/users/<int:pk>/', TodoUserDetailAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
