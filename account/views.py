from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .models import User

def index(request):
    return render(request, 'account/index.html')

def about(request):
    return render(request, 'account/about.html')
def signin(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            User.objects.create_user(email, password)
            return redirect('/login/')
    return render(request, 'account/signin.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)
            auth_login(request, user)

            return redirect('/')

    return render(request, 'account/login.html')
