from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movies.models import Movie
from movies.serializers import MoviesSerializers, MovieDetailSerializers
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions
from rest_framework import views, response, status
from reviews.models import Review
from django.db.models import Avg


class MovieListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Movie.objects.all()
    
    
    def get_serializer_class(self): # request vai bater nesse method para saber qual serializer deve ser usado para serailizar os dados
        if self.request.method == 'GET':
            return MovieDetailSerializers # mostrar os dados formatados usando esse serializer
        return MoviesSerializers # para post usará esse serilizer 

# nota: caso setassemos o mesmo serializer indep do method http, em uma requisição post teriamos que passar dados de obj actors e genres para criar um obj movie
 
# não precisamos setar diretamente o serializer_class para retornar o mesmo serializer independente do method, sobreescrevendo esse method podemos retornar serializers dinâmico dependendo da request.method 

class MoviesRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Movie.objects.all()
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializers
        return MoviesSerializers

    

class MoviesStats(views.APIView): # view criada manualmente (definindo métodos e lógicas) herdando de views.APIView 
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializers


    def get(self, request):
        total_movies = self.queryset.count()
        total_reviews = Review.objects.count()
        average_reviews = Review.objects.aggregate(avg__stars=Avg('stars')['avg_stars'])
        
        '''data={
            'total_movies':total_movies,
            'total_reviewa':total_reviews,
            'avegare_reviews': round(average_reviews, 1) if average_reviews else 0, # if ternário
        }

        serializer = MoviesSerializers(data=data)
        serializer.is_valid(raise_exception=True) # chamaria as func validate do serializer

        return response.Response(data=serializer.validate_data, status=status.HTTP_200_OK)'''
        
        response.Response(data = {
            'total_movies':total_movies,
            'total_reviews':total_reviews,
            'average_reviews': round(average_reviews, 1) if average_reviews else 0, # if ternário
        },status=status.HTTP_200_OK)



# para construirmos uma view que vá alem de uma operação do crud podemos herdar de apiview, assim podendo definir o comportamento dessa view, métodos: get, post, delete e etc