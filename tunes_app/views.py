from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Count

from .models import Album, Track, Artist, Genre

def album_list(request):
    albums = Album.objects.annotate(album_count=Count('artist')).all()
# WHY DO WE HAVE TO USE 'ARTIST' WHEN def bookcase_list DOESN'T???????????

    context = {
        "albums": albums,
    }
    return render(request, "tunes_app/album_list.html", context)

def album_detail(request, id):
    album = get_object_or_404(Album, pk=id)
