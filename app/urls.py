from django.contrib import admin
from django.urls import path
from genres.views import GenreCreatListView,GenreRetriveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenreCreatListView.as_view(), name='genres_create_list_view'),
    path('genres/<int:pk>/',GenreRetriveUpdateDestroyView.as_view(),name='genre-detail-view'), 
]

# o Django vai capturar o valor que aparece no lugar de <int:pk> e passá-lo como um argumento para a função genre_detail_view.
# obs: o para detail, update e delete de um crud, devemos usar na url um identificador que seja único para cada objeto no bd ex: <int:pk>