from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponse

from .models import Album, Track, Artist, Genre

def albums_list(request):
    albums = Album.objects.all()

    context = {
        "albums": albums,
    }
    return render(request, "tunes_app/albums_list.html", context)

def albums_for_artist(request, id):
    specific_artist = get_object_or_404(Artist, pk=id)
    artist_albums = specific_artist.album_set.all()

    context = {
        "specific_artist": specific_artist,
        "artist_albums": artist_albums,
    }
    return render(request, "tunes_app/albums_for_artist.html", context)

def tracks_in_album(request, id):
    specific_album = get_object_or_404(Album, pk=id)
    album_tracks = specific_album.track_set.all()

    context = {
        "specific_album": specific_album,
        "album_tracks": album_tracks,
    }
    return render(request, "tunes_app/album_tracks.html", context)

def artist_list(request):
    artists = Artist.objects.all()

    context = {
        "artists": artists,
    }
    return render(request, "tunes_app/artists_list.html", context)

def genre_list(request):
    genres = Genre.objects.all()

    context = {
        "genres": genres,
    }
    return render(request, "tunes_app/genres_list.html", context)
