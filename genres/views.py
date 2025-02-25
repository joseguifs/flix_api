from django.http import JsonResponse
from genres.models import Genres

def genres_view(request): # primeiro endpoint
    genres = Genres.objects.all() # retorna um queryset com todo objetos do modelo
    data = [{'id': genre.id, 'genres': genre.name} for genre in genres] # serializando meu queryset manualmente
    return JsonResponse(data, safe=False) # safe = False, indicando ao JsonResponse que deve serializar um objeto dict - list e tranforma em json
