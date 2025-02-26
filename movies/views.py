from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movies.models import Movie
from movies.serializers import MoviesSerializers 

class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializers


class MoviesRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializers