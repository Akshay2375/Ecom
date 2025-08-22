from django.shortcuts import render,redirect
from cart.cart import Cart
from .forms import Shippingform 
from.models import ShippingAdress,Order,OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PaymentForm


def orders(request,pk):
    if request.user.is_authenticated and request.user.is_superuser:
        orders=Order.objects.get(pk=pk)
        items=OrderItem.objects.filter(order=pk)
        return render(request,'payments/orders.html',{'order':orders,'items':items}) 
    else:
        messages.success(request," Access Denined ")
        return redirect('home')

def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders=Order.objects.filter(shipped=False)
        return render(request,'payments/not_shipped_dash.html',{'orders':orders}) 
    else:
        messages.success(request," Access Denined ")
        return redirect('home')
def shipped_dash(request):
     orders=Order.objects.filter(shipped=True)
     if request.user.is_authenticated and request.user.is_superuser:
        return render(request,'payments/shipped_dash.html',{'orders':orders })
      
     else:
        messages.success(request,"  Access Denined ")
        return redirect('home')
    
      
def payment_success(request):
    return render(request,'payments/payment_success.html')

def process_order(request):
    
    
    cart=Cart(request)
    quantities=cart.get_quants
    cart_products=cart.get_prods
    totals=cart.cart_total()
    
    if request.POST:
       paymentform=PaymentForm(request.POST or None)
       
       my_shipping=request.session.get('my_shipping')
       full_name=my_shipping['shipping_full_name']
       email=my_shipping['shipping_email']
       amount_paid=totals
       user=request.user
       
       shipping_address=f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n"
       print(shipping_address)
       if request.user.is_authenticated:
           create_order=Order(user=user,full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid)
           create_order.save()
           
           
           order_id=create_order.pk
           
           for product in cart_products():
               
               product_id=product.id
               
               if product.is_sale:
                   price=product.sale_price
                   
               else:
                   price=product.price
           

               for key,value in quantities().items():
                    if int(key)==product.id:
                        create_order_item=OrderItem( user=request.user,product_id=product_id,order_id=order_id,quantity=value,price=price)
                        create_order_item.save()
                        
           for key in list(request.session.keys()):
                if key=='session_key':
                    del request.session['key']
           
           
           
           messages.success(request," Order Placed ")
           return redirect('home')
        
       else:
           create_order=Order( full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid)
           create_order.save()
           
           
           order_id=create_order.pk
           
           for product in cart_products():
               
               product_id=product.id
               
               if product.is_sale:
                   price=product.sale_price
                   
               else:
                   price=product.price
           

               for key,value in quantities().items():
                    if int(key)==product.id:
                        create_order_item=OrderItem(  product_id=product_id,order_id=order_id,quantity=value,price=price)
                        create_order_item.save()
           
           
           for key in list(request.session.keys()):
                if key=='session_key':
                    del request.session['key']
                
                
           
           
           
           messages.success(request," Order Placed ")
           return redirect('home')
       
       
 
        
    else:
         messages.success(request," ACCESS DENIED ")
         return redirect('home')

def billing_info(request):
   if request.method=="POST": 
    cart=Cart(request)
    quantities=cart.get_quants
    cart_products=cart.get_prods
    totals=cart.cart_total()
    shipping_form=request.POST
    
    my_shipping=request.POST
    request.session['my_shipping']=my_shipping
    
    
    
    if request.user.is_authenticated:   
      billing_form=PaymentForm()
      return render(request,'payments/billing_info.html',{'cart_products':cart_products,"quantities":quantities,'totals':totals,'shipping_info':request.POST,'billing_form':billing_form})
    else :
        billing_form=PaymentForm()
        return render(request,'payments/billing_info.html',{'cart_products':cart_products,"quantities":quantities,'totals':totals,'shipping_info':request.POST,'billing_form':billing_form})

   else :
       messages.success(" ACCESS DENIED ")
       return redirect('home')

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


 