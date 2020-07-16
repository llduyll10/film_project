from django.db import models
from film.models import FilmPost

# Create your models here.

class Room(models.Model):
    film = models.ForeignKey('film.FilmPost', related_name='film', on_delete=models.CASCADE)
    date_show = models.DateTimeField(auto_now=False, auto_now_add=False, null = True)
    

class Chair(models.Model):
    status = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    room = models.ForeignKey('Room',related_name='chairs', on_delete=models.CASCADE)
    


        
