# Generated by Django 4.0.2 on 2022-03-29 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_to_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='to_delete',
            new_name='deleted',
        ),
    ]
