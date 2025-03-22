from django.db import models
from genres.models import Genres
from actors.models import Actors

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genres, 
                              on_delete=models.PROTECT,
                              related_name='movies') # protegendo o genêro para não ser deleta caso estiver em uso 
    release_date = models.DateField()
    actors = models.ManyToManyField(Actors, related_name='movies_actors')
    resume = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
# relação ForeignKey: um para muitos (1:N) 1 Gênero pode ser associado a vários Filmes, mas cada Filme só pode ter um único Gênero
# um objeto do model genre pode estar associado a varios objetos do model movies mara um objeto do model movies so pode estar associado a um objeto do model genre

# um campo do tipo chave estrangeira é um campo relacionado a um objeto de outro model que ao ser serializado o django vai usar a chave primária desse objeto para representar ele no formato serializado