from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login')

        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=email)
        if user.exists():
            messages.info(request, 'Email is already taken')
            return redirect('register')
        
        user = User.objects.create(
            first_name=fname,
            last_name=lname,
            username=email
        )

        user.set_password(password)
        user.save()

        messages.success(request, 'Your account created successfully')
        return redirect('home')



    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('login')