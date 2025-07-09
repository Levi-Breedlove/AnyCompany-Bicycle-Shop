from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
  product_name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  product_group = models.IntegerField()
  image_url = models.ImageField(max_length=255)

class Order(models.Model):
  amount = models.DecimalField(max_digits=8, decimal_places=2)
  order_date_time = models.DateTimeField(default=timezone.now)

class Order_Item(models.Model):
  order_number = models.ForeignKey("Order", on_delete=models.CASCADE)
  product_id = models.IntegerField(null=True)
  quantity = models.IntegerField()
  amount = models.DecimalField(max_digits=8, decimal_places=2)