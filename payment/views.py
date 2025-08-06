from django.shortcuts import render
from cart.cart import Cart
from .forms import Shippingform
from.models import ShippingAdress

# Create your views here.
def payment_success(request):
    return render(request,'payments/payment_success.html')


def checkout(request):
    cart=Cart(request)
    quantities=cart.get_quants
    cart_products=cart.get_prods
    totals=cart.cart_total()
    if request.user.is_authenticated:
     shipping_user=ShippingAdress.objects.get(user__id=request.user.id)
        
     shipping_form=Shippingform(request.POST or None,instance=shipping_user)
     return render(request,'payments/checkout.html',{'cart_products':cart_products,"quantities":quantities,'totals':totals,'shipping_form':shipping_form})
    
    else:
          shipping_form=Shippingform(request.POST or None,instance=shipping_user)
          return render(request,'payments/checkout.html',{'cart_products':cart_products,"quantities":quantities,'totals':totals,'shipping_form':shipping_form})


    return render(request,'payments/checkout.html',{'cart_products':cart_products,"quantities":quantities,'totals':totals,'shipping_form':shipping_form})
