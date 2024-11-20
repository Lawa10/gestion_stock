# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutorial.quickstart.views import GroupViewSet

from . import views
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    path('users/create/', views.signup),
    path('users/login/', views.login),
    path('admin/register/', views.register_admin, name='register_admin'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('test_token/', views.test_token),
    path('', include(router.urls)),
]


