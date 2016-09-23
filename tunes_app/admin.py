from django.contrib import admin

from .models import Album, Genre, Track, Artist

admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Artist)