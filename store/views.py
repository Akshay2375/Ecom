from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import forms

from .forms import SignUpForm


# @login_required(login_url='login/')
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

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
 