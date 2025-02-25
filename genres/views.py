from django.http import JsonResponse
import json # lib nativa para lidar com objetos json 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genres

@csrf_exempt
def genres_create_list_view(request): # endpoint que lista/cadastra um genero (GET/POST)
    if request.method == 'GET':
        genres = Genres.objects.all() # retorna um queryset com todo objetos do modelo
        data = [{'id': genre.id, 'genres': genre.name} for genre in genres] # serializando meu queryset manualmente
        return JsonResponse(data, safe=False) # safe = False, indicando ao JsonResponse que deve serializar um objeto dict - list e tranforma em json
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) # capturando o body da requisição que está chegando, decodificando para padrão utf-8, para não quebrar a string, loads vai transformar a string no formato json em um objeto dicionário
        new_genre = Genres(name=data['name']) # criando uma objeto model com o name passado no body e id gerado automaticamente
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id,'name':new_genre.name},status=201
            )
    
@csrf_exempt
def genres_create_recurso(request): # endpoint para cadastrar objeto
    genre = json.loads(request.body.decode('utf-8'))
    new_genre = Genres(name=genre['name'])
    new_genre.save()
    return JsonResponse(
        {
            'id':new_genre.id,
            'name':new_genre.name
        }
    )

def genre_detail_view(request, pk): # endpoint para buscar um objeto específico
    genre = get_object_or_404(Genres, pk=pk) # apis rest devem retornar 404 caso objeto não encontrado no bd
    
    if request.method == 'GET':
        data = {'id':genre.id, 'name':genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save() # salvando no bd
        return JsonResponse(
            {'id':genre.id, 'name':genre.name}
        )
    
def genre_update_recurso(request, pk): # endpoint para editar objeto específico 
    genre = get_object_or_404(Genres, pk=pk)
    data_update = json.loads(request.body.decode('utf-8'))
    genre['name'] = data_update['name']
    genre.save()
    return JsonResponse(
        {
            'id':genre.id,
            'genre':genre.name
        }
    )


def genre_delete_recurso(request, pk):
    genre = get_object_or_404(Genres, pk=pk)
    genre.delete()
