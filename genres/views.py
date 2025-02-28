from rest_framework import generics
from genres.serializers import GenreSerializers
from genres.models import Genres
from django.db.models import Count

class GenreCreatListView(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializers # especifica o serializer que converte os objetos em JSON.

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializers
