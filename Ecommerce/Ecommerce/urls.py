"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# myproject/urls.py
ROOT_API_URL ="api/v1/"
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="pearmonie API",
        default_version="v1",
        description="Welcome to the API for pearmonie Ecomerce API. Please do not use without permissions",
        terms_of_service="https://www.pearmonie.co",
        contact=openapi.Contact(email="support@pearmonie.co"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    #path(ROOT_API_URL+'api/', include('Order_App.urls')),
    path(ROOT_API_URL+'api/auth/', include('Users.urls')),
    path(ROOT_API_URL+'api/products/', include('products.urls')),
    path(ROOT_API_URL+'api/catergory/', include('catergory.urls')),
]


