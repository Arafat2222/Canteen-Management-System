
from django.shortcuts import render
from django.http import*
# Create your views here.
def home(request):
     return render(request, 'Home/home.html')

def about(request):
    return render(request,'About/about.html') 
def breakfast(request):
    return render(request,'Menu/breakfast.html') 

def lunch(request):
    return render(request,'Menu/lunch.html') 

def others(request):
    return render(request,'Menu/others.html') 

def cart(request):
    return render(request,'Cart/cart.html')

def login_signup(request):
    return render(request,'Login_signup/login.html')

        