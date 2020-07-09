from django.db import models
from film.models import FilmPost
# Create your models here.
class ChairPost(models.Model):
    type_chair = models.BooleanField(default=False)
    price = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    status = models.BooleanField(default=False)

class ShowTimePost(models.Model):
    chair  = models.ForeignKey('sale_order.ChairPost', on_delete=models.CASCADE)
    film = models.ForeignKey('film.FilmPost', on_delete=models.CASCADE)
    total_price = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    amount_chair = models.IntegerField(default=0, blank=True, null=True)
    time_show = models.DateTimeField(auto_now=False, auto_now_add=False)
