from django.contrib import admin
from django.urls import path, include

# versionamento de apis

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/',include('genres.urls')), # incluindo todas urls do arquivo urls.py de genre e colocando pré fixo nela de api/v1/
    
    path('api/v1/',include('actors.urls')),
    
    path('api/v1/',include('movies.urls')),

    path('api/v1/',include('reviews.urls')),

    path('api/v1/',include('authentication.urls'))
    #path('api/v2/',include(reviews.urls_2))
]

# o Django vai capturar o valor que aparece no lugar de <int:pk> e passá-lo como um argumento para a função get_object() de RetrieveModelMixin. def get_object(self): pk = self.kwargs.get('pk')  return self.get_queryset().get(pk=pk)
# obs: o para detail, update e delete de um crud, devemos usar na url um identificador que seja único para cada objeto no bd ex: <int:pk>