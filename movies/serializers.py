from rest_framework import serializers
from movies.models import Movie

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie # model onde será extraido os dados
        fields = '__all__' # campos que serão serializados para formato json 

