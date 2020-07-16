from django.db import models
import PIL.Image as Image

# Create your models here.
class Product(models.Model):
    prod_id=models.AutoField(primary_key=True)
    prod_name=models.CharField(max_length=30)
    prod_description=models.CharField(max_length=100)
    prod_price=models.IntegerField()
    prod_category=models.CharField(max_length=20,blank=True)
    prod_publish_date=models.DateField()
    prod_image=models.ImageField(upload_to='images',blank=True)
    

    def __str__(self):
        return self.prod_name

class Cart(models.Model):
    cart_item_id=models.AutoField(primary_key=True)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField()
    product_image=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name