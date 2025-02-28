from django.db import models


NATIONALITY_CHOICES = (
    ('USA','Estados Unidos'), # Na esquerda o valor que ficará no bd e na direita o que será exibido para o User
    ('BRAZIL','Brasil')
)

class Actors(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(
        max_length=50,
        choices=NATIONALITY_CHOICES, # choices define quais strings podem ser usadas nesse campo
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name