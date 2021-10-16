from django.urls import path
from .views import login_view, logout_view, register_view, userProfile, folloUser

urlpatterns = [
    path('login', login_view, name="login_view"),
    path('logout', logout_view, name="logout_view"),
    path('register', register_view, name="register_view"),
    path('single/<str:username>', userProfile, name="userProfile"),
    path('follow/<str:username>', folloUser, name="folloUser"),
]
