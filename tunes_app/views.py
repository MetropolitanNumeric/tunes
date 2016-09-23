from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Count

from .models import Album, Track, Artist, Genre

def album_list(request):
    albums = Album.objects.all()

    context = {
        "albums": albums,
    }
    return render(request, "tunes_app/album_list.html", context)

def track_list(request, id):
    tracks = Track.objects.all()

    context = {
        "tracks": tracks,
    }
    return render(request, "tunes_app/album_tracks.html", context)

#def album_detail(request, id):
#    album = get_object_or_404(Album, pk=id)

#    all_tracks = album.track_set.all()

#    context = {
#        "album": album,
#    }
#    return render(request, "tunes_app/album_tracks.html", context)