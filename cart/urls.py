 
from django.contrib import admin
from . import  views
from django.urls import path,include
 
 
urlpatterns = [
    path('cart_summary',views.cart_summary,name='cart_summary'),
    path('cart_add',views.cart_add,name='cart_add'),
    path('cart_delete',views.cart_delete,name='cart_delete'),
    path('cart_update',views.cart_update,name='cart_update'),
] 
