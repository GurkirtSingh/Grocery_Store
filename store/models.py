from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# a model for grouping the products
class Department(models.Model):
    name = models.CharField()
    

# a model to describe product item
class Product(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=2)
    desc = models.CharField()
    department = models.ManyToManyField(Department)
    priceRate = models.DecimalField(max_digits=2)
    image = models.ImageField()
    quantityType = models.CharField()


# a model for cart item
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    subTotal = models.DecimalField(max_digits=2)
    totalTax = models.DecimalField(max_digits=2)
    total = models.DecimalField(max_digits=2)