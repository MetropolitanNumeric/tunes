from django.shortcuts import render, get_object_or_404

from .models import Album, Track, Artist, Genre

def album_list(request):
    albums = Album.objects.all()

    context = {
        "albums": albums,
    }
    return render(request, "tunes_app/album_list.html", context)

def album_detail(request):
    pass