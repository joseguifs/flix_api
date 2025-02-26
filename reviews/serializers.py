from rest_framework.serializers import ModelSerializer
from reviews.models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review # model onde será extraido os dados
        fields = '__all__' # campos do model que serão serializados para formato json 