from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Album, Comment
from .form import AlbumForm

# Create your views here.
def home(request):
    albumList = Album.objects.all().order_by('-id')
    paginator = Paginator(albumList, 6) # Show 6 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # context = {'albumList':albumList}
    return render(request, 'album/home.html',{'page_obj': page_obj})


def albumDetails(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method=='POST':
        feedback = request.POST.get('feedback')
        comment = Comment.objects.create(album=album, user=request.user ,feedback=feedback)
        return redirect(albumDetails,pk)
    commentList = Comment.objects.filter(album=pk).order_by('-id')
    context = {'album':album,'commentList':commentList}
    return render(request, 'album/single-album.html',context)


def createAlbum(request):
    if request.method=='POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save() 
            return redirect('createAlbum')
        else:
            return redirect('createAlbum')
    else:
        form = AlbumForm()
        albumList = Album.objects.filter(user=request.user).order_by('-id')
        return render(request, 'album/create-album.html',{'form':form,'albumList':albumList})

def deleteAlbum(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method=='POST':
        if album:
            album.delete()
        return redirect('createAlbum')
    else:
        return render(request, 'album/delete-album.html',{'album':album})
