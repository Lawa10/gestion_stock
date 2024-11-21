# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutorial.quickstart.views import GroupViewSet, UserViewSet
from . import views


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    path('admin/register/', views.register_admin, name='register_admin'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('create/', views.signup),
    path('login/', views.login),
    path('set_password/<int:pk>/', views.set_password),
    path('test_token/', views.test_token),
    path('', include(router.urls)),
]

