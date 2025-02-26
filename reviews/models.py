from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='review')
    star = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inerior a 0 estrela'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas')
        ]
    )
    comment = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.movie