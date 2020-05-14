from django.contrib import admin
from django.urls import path, include
from .views import storeHome
urlpatterns = [
    path('', storeHome, name='storeHome'),
]
