from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from genres.serializers import GenreSerializers
from genres.models import Genres
from actors.models import Actors 

class MoviesSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True) # campo calculado (campo que não está na minha tabela movie) que será adicionado nas resposta json mas que não está na tabela movie

    # read_only=True define que o campo so pode adicinado no json para resposta/leituras (get)

    # função que vai calcular o valor do campo rate deve começar com get_<nome_do_campo>
    def get_rate(self, obj): # obj será o objeto/registro da tabela que estará sendo serializado
        rate = obj.reviews.aggregate(Avg('stars'))['stars__Avg'] # if 

        if rate:
            return rate
        return None      
    class Meta:
        model = Movie # model onde será extraido os dados
        fields = '__all__' # campos que serão serializados para formato json 


    # função de validação de campo
    def validate_resume(self, value): # value é o parametro que receberá como argumento o valor passado pro campo que queremos validar
        if value.lower() == 'teste':
            raise serializers.ValidationError('não pode ser teste')
        return value
    
    def validate_release_date(self, value):
        if value.year < 2000:
            raise serializers.ValidationError('Filme muito antigo')
        return value
    # caso um campo do json marcado como inválido, logo todo o json é inválido

class MovieStatsSerializer(serializers.Serializer): # EX de serializer para usar em um endpoint feito na mão (desnecessário)
    total_movies = serializers.IntegerField()
    total_reviwes = serializers.IntegerField()
    average_stars = serializers.FloatField() 


# Como escrever um serializer para os campos meu models Movie manualmente
class MmovieSerializers(serializers.Serializer):
    id = serializers.IntegerField() 
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset = Genres.objects.all()
    ),
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset = Actors.objects.all(),
        many=True
    ),
    resume = serializers.CharField()


# review = obj.reviews.all(): reviews ´o nome da relação de chave estrangeira de um campo da tablela movies. obj é o registro/linha da tabela movie que está sendo serializado. Essa linha vai pegar o obj de movie, ir no campo de chave estrangeira da tabela reviews e ver se esse campo está relacionado ao objeto que esta sendo serailizado. <Montará um queryset com os objetos que atendem a esse requisito>

# selecionamos obj de um model e estamos buscando em outro model objetos que tenham o campo de chave estrangeira relacionado a esse objeto

# 2 models a e b, a tem campos normais, b tem um campo de chave estrangeira para a, se selecionarmos um objeto de a e dermos: obj.<nome da relação de chave estrangeira> do campo de chave estrangeira do model b, irá retornar todos os obj do model b que tem o campo de chave estrangeira associado ao obj selecionado 