from rest_framework import serializers
from genres.models import Genres

class GenreSerializers(serializers.ModelSerializer):

    number_movies = serializers.SerializerMethodField(read_only = True)

    def get_number_movies(self, obj):
        movies = obj.movies.count() # rodar makemigrations e migrate 
        if movies:
            return movies
        return None
    class Meta:
        model = Genres
        fields = ['id','name'] # Serializa todos os campos do nosso banco de dados

# SE UTLIZASSEMOS serializers.Serializers teriamos que escrever todos os campos do model manualmente: name = serializers.Charfield(max..). Com o ModelSerializer basta apenas passar os camposdo nosso model em fields: __all__ ou ['campo1','campo2']