from django.contrib import admin
from django.urls import path
from .views import loginUser, signupUser, loginTrouble, logoutUser
urlpatterns = [
    path('login/', loginUser, name = 'login'),
    path('signup/', signupUser, name = 'signup'),
    path('logintrouble/', loginTrouble, name = 'logintrouble'),
    path('logout/', logoutUser, name = 'logout'),
]