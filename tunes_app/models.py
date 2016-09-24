from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist')
    genre = models.ForeignKey('Genre')
#    tracks = models.ForeignKey('Track')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tunes_app:album_detail', args=[self.pk])

class Track(models.Model):
    name = models.CharField(max_length=50)
    albums = models.ForeignKey('Album')
#   Track has multiple albums

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('namespace:name', args=[self.pk])
        pass

class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name