from django.contrib import admin
from django.urls import path, include
from .views import storeHome, productsByDepartment, productDetails, CartItems

urlpatterns = [
    path('', storeHome, name='storeHome'),
    path('department/<str:department>', productsByDepartment, name='productsByDepartment'),
    path('product/<int:productId>', productDetails, name='productDetails'),
    path('cart', CartItems.as_view(), name='cart'),
]