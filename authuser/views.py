# from typing import Generic
# from django.http import request
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .models import Followers, User
from album.models import Album
from django.contrib.auth.forms import PasswordChangeForm
from authuser.form import MyUserCreationForm, UserUpdateForm

# Create your views here.
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your are successfully login')
            return redirect('home')
        else:
            messages.error(request, 'Your login credentials are wrong')
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

@login_required(login_url='login_view')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {
        'form': form
    })

def updateProfile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('userProfile', request.user)
    else:
        form = UserUpdateForm(instance=request.user)

    context={'form': form}
    return render(request, 'profile.html',context )


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



