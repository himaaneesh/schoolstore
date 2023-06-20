from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import newform


# Create your views here.
from requests import auth

# def base(request):
#     return render(request,"base.html")

def index(request):
    return render(request,"index.html")

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            if username and password:
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                return redirect('/')

            error_message = "Invalid login credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

        return render(request, "login.html")

def register(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if username and password and confirm_password:
                if password == confirm_password:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    return render(request,"login.html")

                error_message = "Passwords do not match. Please try again."
                return render(request, 'register.html', {'error_message': error_message})

            error_message = "Please fill in all the required fields."
            return render(request, 'register.html', {'error_message': error_message})

        return render(request,"register.html")


def home(request):
    form = newform()
    return render(request, 'home.html', {'form': form})

def confirm_order(request):
    if request.method == 'POST':
        form = newform(request.POST)
        if form.is_valid():
            return render(request, 'confirm.html')
    else:
        form = newform()
    return render(request, 'home.html', {'form': form})


def logout(request):
    return redirect('/')