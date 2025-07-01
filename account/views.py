from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from shopy.models import *



# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user using the custom user model
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')  # Change to any page you want to redirect after successful login
        else:
            messages.error(request, "Invalid username or password.")  # More specific error message

    return render(request, 'account/login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        phone_field = request.POST.get('phone_field', '').strip()

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('user_register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('user_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('user_register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('user_register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        customer = Customer(user=user, phone_field=phone_field)
        customer.save()

        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('/')
    return render(request, 'account/register.html')

# In user_register
def user_logout(request):
    logout(request)
    return redirect('/')