from itertools import product
from venv import create
from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        product=Product.objects.all()
        context={'product':product,'order':order,'items':items}
    else:
        product=Product.objects.all()
        context={'product':product,'items':0,'order':0}
        
         
    return render(request, 'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        context={'order':order,'items':items}
    else:
        context={'order':0,'items':0}
    return render(request, 'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        context={'order':order,'items':items}
    else:
        context={'order':0,'items':0}
    return render(request, 'store/checkout.html',context)

def update_item(request):
   
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
  

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0  :
        orderItem.delete()
  
    elif action=='delete':
        orderItem.delete()
     

    return JsonResponse('Item was added', safe=False)

def register(request):
    form=UserCreationForm()
    context={'form':form}
    
    
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
                user=form.save()
                Customer.objects.create(user=user,name='vide',email='vide@vv')
                return redirect('/')
                
        
          
        
                

    
    return render(request, 'registration/register.html',context)