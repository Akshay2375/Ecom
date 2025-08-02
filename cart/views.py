from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from store.models import Product
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    quantities=cart.get_quants
    cart_products=cart.get_prods
    totals=cart.cart_total()
    
    return render(request,'cart_summary.html',{'cart_products':cart_products,"quantities":quantities,'totals':totals})




def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product=get_object_or_404(Product,id=product_id)
        
        
        cart.add(product=product,quanity=product_qty)
        
        car_quanity=cart.__len__()
        response=JsonResponse({"qty":car_quanity})
        messages.success(request,(" Product added to cart  "))

    return response
     

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        
        cart.delete(product=product_id)
        messages.success(request,(" Product removed from cart  "))

    return JsonResponse({'product': product_id})

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')

        if not product_qty or not product_qty.isdigit():
            return JsonResponse({'error': 'Invalid quantity'}, status=400)

        product_qty = int(product_qty)
        cart.update(product=product_id, quantity=product_qty)
        messages.success(request,(" Cart Updated  "))
        return JsonResponse({'qty': product_qty})

    return JsonResponse({'error': 'Invalid request'}, status=400) 