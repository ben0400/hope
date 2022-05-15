from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.store,name='store'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('update_item/',views.update_item,name='update_item'),
    path('register',views.register,name='register'),
    path('index',views.index,name='index'),
    
]
