
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, re_path
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework_swagger.views import get_swagger_view


schema_view = get_schema_view(
   openapi.Info(
      title="Gestion_Stock API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('category/', include('category.urls')),
    path('subcategory/', include('subcategory.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
