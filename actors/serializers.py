from rest_framework import serializers
from actors.models import Actors

class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'

    movies_autor = serializers.SerializerMethodField(read_only = True)

    def get_movies_autor(self, obj):
        movies_autor = obj.movies_actors

        if movies_autor:
            return movies_autor
        return False