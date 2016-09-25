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

#   Tracks in a specific album
    album_tracks = Album.track_set
    tracks = Track.objects.all()

    context = {
        "specific_album": specific_album,
        "album_tracks": album_tracks,
        "tracks": tracks,
    }
    return render(request, "tunes_app/album_tracks.html", context)
