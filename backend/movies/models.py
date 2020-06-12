from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    video = models.BooleanField()
    overview = models.TextField()
    original_language = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=1000)
    backdrop_path = models.CharField(max_length=1000)
    genres = models.ManyToManyField(Genre, related_name='movies')

class Rating(models.Model):
    movie = models.ForeignKey(Movie, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='ratings')
    score = models.FloatField()