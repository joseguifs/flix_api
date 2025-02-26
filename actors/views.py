from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from actors.models import Actors
from actors.serializers import ActorsSerializers

class ActorsListCreateView(ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers

class ActorsRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers



