from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# a model for grouping the products
class Department(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="departments", null=True)

    def __str__(self):
        return self.name
    


# a model to describe product item
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
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
    subTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalTax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    createdDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'cart for {self.user.email}')

class OrderItem(models.Model):
    orderCart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} {self.item.name}'