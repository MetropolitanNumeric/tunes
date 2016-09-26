from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.albums_list, name='albums_list'),
    url(r'^artist/$', views.artist_list, name='artist_list'),
    url(r'^genre/$', views.genre_list, name='genre_list'),
    url(r'^(?P<id>\d+)/$', views.tracks_in_album, name='tracks_in_album'),
]