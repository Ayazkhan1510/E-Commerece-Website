# Generated by Django 4.2.5 on 2023-09-28 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price']},
        ),
    ]
