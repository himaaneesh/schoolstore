from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from requests import auth

# def base(request):
#     return render(request,"base.html")

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request,"register.html")

def newpage(request):
    return render(request,"newpage.html")

def order_confirmation(request):
    if request.method == 'POST':
        confirmation_message = "Order is confirmed!"
        return render(request, 'confirm.html', {'confirmation_message': confirmation_message})
    return render(request, "newpage.html")

def logout(request):
    # logout(request)
    return redirect('/')