# Generated by Django 5.1.1 on 2024-09-23 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergory', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_catergory', to='catergory.category'),
        ),
        migrations.RemoveField(
            model_name='products',
            name='Price',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
