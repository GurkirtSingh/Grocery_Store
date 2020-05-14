from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def loginUser(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

def signupUser(request):
    if request.method != 'POST':
        return render(request, 'accounts/signup.html')
