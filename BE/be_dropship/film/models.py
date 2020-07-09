from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
	file_path = 'film/{author_id}/{title}-{filename}'.format(
			author_id=str(instance.author.id), title=str(instance.title), filename=filename
		) 
	return file_path

class FilmPost(models.Model):
    title = models.CharField(max_length=100, null=False, blank=True)
    directors = models.CharField(max_length=100, null=False, blank=True)
    urlFilm = models.CharField(max_length=1000,null=False, blank=True)
    date_published = models.DateTimeField(auto_now_add=True,verbose_name='date published',blank=True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date update')
    contentFilm = models.CharField(max_length=500, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', null=False, blank=True)
    typeFilm = models.CharField(max_length=100, null=False, blank=True)
    # def __str__(self):
    #     return self.title
    
@receiver(post_delete, sender=FilmPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_film_post_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + '-' + instance.title)

pre_save.connect(pre_save_film_post_receiever, sender=FilmPost)



