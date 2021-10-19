from django.urls import path
from .views import login_view, logout_view, register_view, userProfile, folloUser, change_password, updateProfile

urlpatterns = [
    path('login', login_view, name="login_view"),
    path('logout', logout_view, name="logout_view"),
    path('register', register_view, name="register_view"),
    path('password/', change_password, name='change_password'),
    path('profile/edit', updateProfile, name='updateProfile'),
    path('single/<str:username>', userProfile, name="userProfile"),
    path('follow/<str:username>', folloUser, name="folloUser"),
]
