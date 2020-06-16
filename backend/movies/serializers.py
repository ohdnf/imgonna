from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie, Rating


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')


class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Rating
        fields = '__all__'