from django.db import models


# Create your models here.

class FavouriteMovie(models.Model):
    id = models.IntegerField(),
    movieId = models.IntegerField(default=-1)
    posterPath = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)
