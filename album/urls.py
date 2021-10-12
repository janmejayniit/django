from django.urls import path
from .views import home, albumDetails


urlpatterns=[
    path('', home, name='home'),
    path('album/<int:pk>', albumDetails, name='albumDetails'),
]