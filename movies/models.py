from django.db import models
from genres.models import Genres
from actors.models import Actors

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genres, 
                              on_delete=models.PROTECT,
                              related_name='movies') # protegendo o genêro para não ser deleta caso estiver em uso 
    release_date = models.DateField()
    actors = models.ManyToManyField(Actors, related_name='movies')
    resume = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title