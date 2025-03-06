from django.db import models

# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=100)
    number_movies = models.IntegerField(null=True) # transformar para campo computado depois 

    def __str__(self):
        return self.name