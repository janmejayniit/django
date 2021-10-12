from django.shortcuts import render
from .models import Album, Comment

# Create your views here.
def home(request):
    albumList = Album.objects.all()
    context = {'albumList':albumList}
    return render(request, 'album/home.html',context)


def albumDetails(request, pk):
    album = Album.objects.get(pk=pk)
    commentList = Comment.objects.filter(album=pk)
    context = {'album':album,'commentList':commentList}
    return render(request, 'album/single-album.html',context)