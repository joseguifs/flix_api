from rest_framework import serializers
from genres.models import Genres

class GenreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__' # Serializa todos os campos do nosso banco de dados