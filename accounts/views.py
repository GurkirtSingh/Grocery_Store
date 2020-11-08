from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('storeHome')
        else:
            context = {
                'error': 'Invalid credentials',
                'username': username,
                'password': password
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    print('logout')
    return redirect('login')

def signupUser(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            user = User.objects.create_user(
                username=username,
                email=username,
                first_name=firstname,
                last_name=lastname,
                password=password)
            if user is not None:
                return redirect('storeHome')
            else:
                return render(request, 'account/signup.html', {'error': 'Invalid Fields'})
        else:
                return render(request, 'account/signup.html', {'error': 'Password does not match'})
    else:
        return render(request, 'accounts/signup.html')
def loginTrouble(request):
    return render(request, 'accounts/logintrouble.html')
