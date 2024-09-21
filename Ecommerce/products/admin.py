from django.contrib import admin
from django.contrib.auth.models import Group

from products.models import Products, Category
# Register your models here.
admin.site.register(Products)
admin.site.register(Category)


