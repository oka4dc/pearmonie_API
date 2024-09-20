from django.contrib import admin
from Users.models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Register your models here.

admin.site.register(CustomUser)

