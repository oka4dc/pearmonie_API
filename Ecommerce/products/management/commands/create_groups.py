from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from products.models import Product

class Command(BaseCommand):
    help = 'Create default user groups'

    def handle(self, *args, **kwargs):
        sellers_group, created = Group.objects.get_or_create(name='Sellers')
        Buyers_group, created = Group.objects.get_or_create(name='Buyers')
        Admin_group, created = Group.objects.get_or_create(name='Admin')
        
         # Assign permissions to Sellers group
        content_type = ContentType.objects.get(app_label='products', model='product')
        add_product_permission = Permission.objects.get(codename='add_product', content_type=content_type)
        change_product_permission = Permission.objects.get(codename='change_product', content_type=content_type)

        sellers_group.permissions.add(add_product_permission, change_product_permission)

        # Assign permissions to Buyers group
        view_product_permission = Permission.objects.get(codename='view_product', content_type=content_type)
        Buyers_group.permissions.add(view_product_permission)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions.'))