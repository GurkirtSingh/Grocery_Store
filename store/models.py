from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# a model for grouping the products
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

# a model to describe product item
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.CharField(max_length=300)
    department = models.ManyToManyField(Department)
    priceRate = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    quantityType = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# a model for cart item
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    subTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalTax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return (f'cart for {self.user.email}')