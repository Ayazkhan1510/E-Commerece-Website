from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=30, default="")
    sub_category = models.CharField(max_length=30,default="")
    product_desc = models.CharField(max_length=300)
    price = models.IntegerField(max_length=8,default=0)
    publish_date = models.DateField()
    images = models.ImageField(upload_to='shop/images',default="")
    class Meta:
        ordering=['price']