from rest_framework import serializers
from actors.models import Actors

class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'