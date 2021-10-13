from django.urls import path
from .views import home, albumDetails, createAlbum, deleteAlbum


urlpatterns=[
    path('', home, name='home'),
    path('album/add', createAlbum, name='createAlbum'),
    path('album/<int:pk>', albumDetails, name='albumDetails'),
    path('album/delete/<int:pk>', deleteAlbum, name='deleteAlbum'),
]