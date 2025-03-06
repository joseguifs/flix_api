from rest_framework import generics
from genres.serializers import GenreSerializers
from genres.models import Genres
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions
from movies.models import Movie

class GenreCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializers # especifica o serializer que converte os objetos em JSON.
    print(Genres.objects.values())
    print(Movie.objects.values('genre__name'))

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializers
