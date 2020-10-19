from django.contrib import admin
from accounts.models import Customer
from store.models import *

# Register your models here.
admin.site.register([Customer, Department, Product, Cart, OrderItem])
