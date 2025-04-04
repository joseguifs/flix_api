from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from genres.models import Genres
from movies.models import Movie


def update_number_movies(movie):
    id = movie.genre.id
    genre = Genres.objects.get(id=id)
    genre.number_movies = Movie.objects.filter(genre__name__icontains=genre).count() # corrigir pois o icontains espera um argumento do tipo string 
    genre.save()

@receiver(post_save, sender=Movie)
def genre_post_save(sender, instance, **kwargs):
    update_number_movies(instance)

@receiver(post_delete, sender=Movie)
def genre_post_delete(sender, instance, **kwargs):
    update_number_movies(instance)

# instance.genre é o objeto completo do modelo Genre, e não apenas o id ou o name. Você pode acessar todos os campos do objeto Genre através de instance.genre, como por exemplo instance.genre.name, instance.genre.id

# Movie.objects.filter(genre__name__icontains=genre).count(): criamos um filtro para os objetos da tabela Movie e o count() faz uma busca no bd contando objetos que atendam a esse filtro 