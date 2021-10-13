from typing import Generic
from django.http import request
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout

from authuser.form import MyUserCreationForm

# Create your views here.
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_view')
    else:
        if request.user.is_authenticated:
           return redirect('home')
        return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')


def register_view(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
            return redirect('register_view')
    else:
        if request.user.is_authenticated:
           return redirect('home')
        return render(request, 'auth/register.html', {'form': form})


def userProfile(request):
    return render(request, 'user.html')