from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorit = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.email
