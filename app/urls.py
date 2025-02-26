from django.contrib import admin
from django.urls import path
from genres.views import GenreCreatListView,GenreRetriveUpdateDestroyView
from actors.views import ActorsListCreateView, ActorsRetriveUpdateDestroyView
from movies.views import MovieListCreateView, MoviesRetriveUpdateDestroyView
from reviews.views import ReviewListCreateView, ReviewRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/',GenreCreatListView.as_view(), name='genres_view'), # get daqui chama o método list(self.list)
    path('genres/<int:pk>/',GenreRetriveUpdateDestroyView.as_view(),name='genre_rud'), # get aqui chama o método retrive(self.retrive) 
    
    path('actors/',ActorsListCreateView.as_view(),name='actors_view'),
    path('actors/<int:pk>/',ActorsRetriveUpdateDestroyView.as_view(),name='actors_rud'),

    path('movies/',MovieListCreateView.as_view(), name='movie_view'),
    path('movies/<int:pk>/', MoviesRetriveUpdateDestroyView.as_view(), name='movie_rud'),

    path('review/',ReviewListCreateView.as_view(),name='review_view'),
    path('review/<int:pk>', ReviewRetriveUpdateDestroyView.as_view(), name='review_rud')
]

# o Django vai capturar o valor que aparece no lugar de <int:pk> e passá-lo como um argumento para a função get_object() de RetrieveModelMixin. def get_object(self): pk = self.kwargs.get('pk')  return self.get_queryset().get(pk=pk)
# obs: o para detail, update e delete de um crud, devemos usar na url um identificador que seja único para cada objeto no bd ex: <int:pk>