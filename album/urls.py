from django.urls import path
from .views import home, albumDetails, createAlbum, deleteAlbum, albumLike, albumDisLike


urlpatterns=[
    path('', home, name='home'),
    path('album/add', createAlbum, name='createAlbum'),
    path('album/<int:pk>', albumDetails, name='albumDetails'),
    path('album/delete/<int:pk>', deleteAlbum, name='deleteAlbum'),
    path('album/like/<int:pk>', albumLike, name='albumLike'),
    path('album/dislike/<int:pk>', albumDisLike, name='albumDisLike'),
]