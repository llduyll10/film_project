from rest_framework import serializers
from film.models import FilmPost

import os
from django.conf import settings
from django.core.files.storage import default_storage, FileSystemStorage

IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2 #2MB
MIN_TITLE_LENGTH = 5
MIN_CONTENT_LENGTH = 50

# Create
class FilmPostCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = FilmPost
        fields = ['pk', 'title', 'directors', 'urlFilm', 'date_published', 'contentFilm', 'slug', 'image', 'author','typeFilm']
    
    def save(self):
        try:
            image = self.validated_data['image']
            title = self.validated_data['title']
            directors = self.validated_data['directors']
            urlFilm = self.validated_data['urlFilm']
            typeFilm = self.validated_data['typeFilm']
            if len(title) < MIN_TITLE_LENGTH:
                raise serializers.ValidationError({'response':'Enter a title longer than ' + str(MIN_TITLE_LENGTH) + 'characters.'})
            contentFilm = self.validated_data['contentFilm']
            if len(contentFilm) < MIN_CONTENT_LENGTH:
                raise serializers.ValidationError({'response':'Enter a content film longer than ' + str(MIN_CONTENT_LENGTH) + 'characters.'})
            film_post = FilmPost(
                author = self.validated_data['author'],
                title = title,
                directors = directors,
                urlFilm = urlFilm,
                contentFilm = contentFilm,
                image = image,
                typeFilm = typeFilm
            )
            film_post.save()
            return film_post
        except KeyError:
            raise serializers.ValidationError({"response": "You must have a title, some content, and an image."})

# Update
class FilmPostUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = FilmPost
        fields = ['title', 'directors', 'urlFilm', 'contentFilm', 'image', 'typeFilm']
    def validate(self, film_post):
        try:
            title = film_post['title']
            if len(title) < MIN_TITLE_LENGTH:
                raise serializers.ValidationError({'response':'Enter a title longer than ' + str(MIN_TITLE_LENGTH) + 'characters.'})
            contentFilm = film_post['contentFilm']
            if len(contentFilm) < MIN_CONTENT_LENGTH:
                raise serializers.ValidationError({'response':'Enter a content film longer than ' + str(MIN_CONTENT_LENGTH) + 'characters.'})
        except KeyError:
            pass
        return film_post

# Get detail
class FilmPostSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')
    class Meta:
        model = FilmPost
        fields = ['pk', 'title', 'directors', 'urlFilm', 'date_published', 'contentFilm', 'slug', 'image', 'username', 'typeFilm']
    
    def get_username_from_author(self, film_post):
        username = film_post.author.username
        return username



