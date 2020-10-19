from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Department, Product, Cart, OrderItem
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

# Create your views here.
@login_required(login_url='login')
def storeHome(request):
    user = request.user
    departments = Department.objects.all()
    context = {
        'username': user.first_name,
        'departments': departments
    }
    return render(request, 'store/home.html', context)

@login_required(login_url='login')
def productsByDepartment(request, department):
    allSections = Department.objects.all()
    products = Product.objects.all().filter(department__name__contains=department)
    context = {
        'products': products,
        'sections': allSections
    }
    return render(request, 'store/itemList.html', context)
@login_required(login_url='login')
def productDetails(request, productId):
    product = Product.objects.get(pk=productId)
    cart, created = Cart.objects.get_or_create(user=request.user)
    orderItem = OrderItem.objects.filter(orderCart=cart, item=product)
    context = {}
    context['product'] = product
    context['quantInCart'] = 1
    if orderItem.count() >= 1:
        context['quantInCart'] = orderItem[0].quantity
    print(context)
    return render(request, 'store/itemDetail.html', context)


class CartItems(View):

    @method_decorator(login_required)
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = OrderItem.objects.filter(orderCart=cart)
        return render(request, 'store/cartDetails.html', {'items': items})
    @method_decorator(login_required)
    def post(self, request):
        id = request.POST['id']
        numberOf = request.POST['quant']
        action = request.POST['action']

        product = Product.objects.get(pk=id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        ordetItem, created = OrderItem.objects.get_or_create(orderCart=cart,item=product)
        if action == 'PUT':
            ordetItem.quantity = numberOf
            ordetItem.save()
            return JsonResponse({'added':True })
        elif action == 'REMOVE':
            ordetItem.delete()
            return JsonResponse({'removed':True })

