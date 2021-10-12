from django.shortcuts import render
from .models import Album

# Create your views here.
def home(request):
    albumList = Album.objects.all()
    context = {'albumList':albumList}
    return render(request, 'album/home.html',context)


def albumDetails(request, pk):
    album = Album.objects.get(pk=pk)
    context = {'album':album}
    return render(request, 'album/single-album.html',context)