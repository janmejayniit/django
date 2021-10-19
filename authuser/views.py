from typing import Generic
from django.http import request
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .models import Followers, User
from album.models import Album

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
            user.is_staff = True
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


def userProfile(request, username):
    user = User.objects.get(username=username)
    albumList = Album.objects.filter(user=user).order_by('-id')
    totalFollower = Followers.objects.filter(user=user).count()
    followersList = Followers.objects.filter(user=user).values_list('follow_user',flat=True)
    context = {'user':user, 'albumList':albumList,'totalFollower':totalFollower,'followersList':followersList}
    return render(request, 'user.html', context)


def folloUser(request, username):

    if request.method=='POST':
        user = User.objects.get(username=username)
        obj=Followers.objects.create(user=user, follow_user=request.user)
        return redirect('userProfile', username)



