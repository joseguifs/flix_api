from django.http import JsonResponse
import json # lib nativa para lidar com objetos json 
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genres

@csrf_exempt
def genres_view(request): # primeiro endpoint
    if request.method == 'GET':
        genres = Genres.objects.all() # retorna um queryset com todo objetos do modelo
        data = [{'id': genre.id, 'genres': genre.name} for genre in genres] # serializando meu queryset manualmente
        return JsonResponse(data, safe=False) # safe = False, indicando ao JsonResponse que deve serializar um objeto dict - list e tranforma em json
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) # capturando o body da requisição que está chegando, decodificando para padrão utf-8, para não quebrar a string, loads vai transformar a string no formato json em um objeto dicionário
        new_genre = Genres(name=data['name'])
        new_genre.save()
        return JsonResponse({
            'id': new_genre.id,
            'name':new_genre.name,
        },status=201)