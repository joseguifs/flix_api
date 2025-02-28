from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializers

class MoviesSerializers(serializers.ModelSerializer):
    genre = GenreSerializers() # Ao serializar o modelo Movie, ele deve usar o GenreSerializers para o campo genre, em vez de apenas serializar o ID.
    class Meta:
        model = Movie # model onde será extraido os dados
        fields = '__all__' # campos que serão serializados para formato json 

