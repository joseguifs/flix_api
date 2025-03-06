from django.urls import path
from . import views

urlpatterns = [
    path('genres/',views.GenreCreatListView.as_view(), name='genres_view'), # get daqui chama o método list(self.list)
    path('genres/<int:pk>/',views.GenreRetriveUpdateDestroyView.as_view(),name='genre_rud'),
]

# caso queira adicionar mais urls/endpoint só precisa coloca-la nesse arquivo
# caso lançarmos um v2 da nossa api, criaremos um arquivo com novos endpoints/urls(recurso) e incluiremos ele la no urls de app sem acabar com a v1 da nossa api