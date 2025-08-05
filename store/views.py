from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Product,Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import forms
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q
from .forms import SignUpForm,UpdateUserForm,ChangePassword,UserInfoForm

from payment.forms import Shippingform
from payment.models import ShippingAdress

import json
from cart.cart import Cart
# @login_required(login_url='login/')
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})


def product(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'product.html',{'product':product})

def about(request):
    return render(request,'about.html',{})

def login_user(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            current_user=Profile.objects.get(user__id=request.user.id)
            saved_cart=current_user.old_cart
            if saved_cart:
                converted_cart=json.loads(saved_cart)
                cart=Cart(request)
                
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)
                
            messages.success(request,(" YOU ARE LOGGED IN "))
            return redirect('home')
        else:
             messages.success(request,(" INVALID CREDENTIALS  "))
             return redirect('login')
    else:
        return render(request,"login.html")

     
def logout_user(request):

    logout(request)
    messages.success(request,(" LOGEED OUT  "))
    return redirect('login')

def search(request):
    if request.method=='POST':
        searched=request.POST['searched']
        searched=Product.objects.filter(Q(name__icontains=searched)|Q(description__icontains=searched))
        if not searched:
            messages.success(request,(" nothing found  "))
            return render(request,"search.html")
        else:
         return render(request,"search.html",{'searched':searched})
    else:
     return render(request,"search.html")
def register_user(request):
    form=SignUpForm()

    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,(" U HAVe become a user  "))
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("please enter the info  "))
            return redirect('update_info')
        else:
         messages.success(request,(" Problem REGISTER AGAIN  "))
         return redirect('register')
    else:


     return render(request,"registration.html",{'form':form})
 
def category(request,foo):
    foo=foo.replace('-',' ')
    try:
     category=Category.objects.get(name=foo)
     products=Product.objects.filter(category=category)
    
     return render(request,"category.html",{'products':products,'category':category})
    except Category.DoesNotExist:
         
      messages.success(request,(" NO SUch Category  "))
      return redirect('home')
    

def category_summary(request):
         categories=Category.objects.all()
         return render(request,"category_summary.html",{'categories':categories})



def update_info(request):
     if request.user.is_authenticated:
        current_user=Profile.objects.get(user__id=request.user.id)
        shipping_user=ShippingAdress.objects.get(user__id=request.user.id)
        form=UserInfoForm(request.POST or None,instance=current_user)
        
        shipping_form=Shippingform(request.POST or None,instance=shipping_user)
        if form.is_valid() or shipping_form :
            form.save()
            shipping_form.save()
            
            messages.success(request,"  INfo  HAS BEEN UPDATE")
            return redirect('home')
        return render(request,'update_info.html',{'form':form,'shipping_form':shipping_form})
     else:
            messages.success(request," login")
            return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None,instance=current_user)
        
        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(" USER HAS BEEN UPDATE")
            return redirect('home')
        return render(request,'update_user.html',{'user_form':user_form})
    else:
            messages.success(" login")
            return redirect('home')
def update_password(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = ChangePassword(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Password updated.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = ChangePassword(user)
            return render(request, 'update_password.html', {"form": form})
    else:
        messages.success(request, "Login first.")
        return redirect('login')  # ✅ Add this line
