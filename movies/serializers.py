from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator')

    def validate(self, data):
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to create a movie")
        return data


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
