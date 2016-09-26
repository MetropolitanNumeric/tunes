from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Count

from .models import Album, Track, Artist, Genre

def albums_list(request):
    albums = Album.objects.all()

    context = {
        "albums": albums,
    }
    return render(request, "tunes_app/albums_list.html", context)

def tracks_in_album(request, id):
    specific_album = get_object_or_404(Album, pk=id)
    album_tracks = specific_album.track_set.all()

    context = {
        "specific_album": specific_album,
        "album_tracks": album_tracks,
    }
    return render(request, "tunes_app/album_tracks.html", context)
