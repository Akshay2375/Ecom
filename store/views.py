from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Product,Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import forms
from django.contrib.auth.models import User

from .forms import SignUpForm,UpdateUserForm


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
            return redirect('home')
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


 