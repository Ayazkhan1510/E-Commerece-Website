# Generated by Django 4.2.5 on 2023-09-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category_product_images_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]