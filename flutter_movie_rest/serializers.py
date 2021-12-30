from rest_framework import serializers
from django.contrib.auth.models import User

from flutter_movie_rest.models import FavouriteMovie


class FavouriteMovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FavouriteMovie
        fields = ['id', 'movieId', 'posterPath', 'owner']


class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=FavouriteMovie.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'movies']
