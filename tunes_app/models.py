from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist')
    genre = models.ForeignKey('Genre')

    def get_absolute_url(self):
        #return reverse('namespace:name', args=[self.pk])
        pass

class Track(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey('Album')

    def get_absolute_url(self):
        #return reverse('namespace:name', args=[self.pk])
        pass

class Artist(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=50)