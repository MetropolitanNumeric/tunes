from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^albums/$', views.album_list, name='album_list'),
    url(r'^artists/$', views.artist_list, name='artist_list'),
    url(r'^genres/$', views.genre_list, name='genre_list'),
    url(r'^albums/(?P<id>\d+)/$', views.album_detail, name='album_detail'),
    url(r'^artists/(?P<id>\d+)/$', views.artist_detail, name='artist_detail'),
]