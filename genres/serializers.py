from rest_framework import serializers
from genres.models import Genres

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id','name','number_movies'] # Serializa todos os campos do nosso banco de dados

# SE UTLIZASSEMOS serializers.Serializers teriamos que escrever todos os campos do model manualmente: name = serializers.Charfield(max..). Com o ModelSerializer basta apenas passar os camposdo nosso model em fields: __all__ ou ['campo1','campo2']