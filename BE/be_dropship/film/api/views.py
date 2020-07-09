from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from account.models import Account
from film.models import FilmPost
from .serializers import FilmPostCreateSerializers, FilmPostUpdateSerializers, FilmPostSerializers

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Url: https://<your-domain>/api/film/create
# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_film(request):
    if request.method == 'POST':
        data = request.data
        data['author'] = request.user.pk
        checkExists = FilmPost.objects.filter(
            title=request.data['title']).count()
        if checkExists > 0:
            return Response({'status': 'error', 'msg': 'Title is available'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FilmPostCreateSerializers(data=data)
        data = {}
        if serializer.is_valid():
            film_post = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['pk'] = film_post.pk
            data['title'] = film_post.title
            data['directors'] = film_post.directors
            data['urlFilm'] = film_post.urlFilm
            data['date_published'] = film_post.date_published
            data['contentFilm'] = film_post.contentFilm
            data['slug'] = film_post.slug
            data['typeFilm'] = film_post.typeFilm
            image_url = str(request.build_absolute_uri(film_post.image.url))
            data['image'] = image_url
            data['author'] = film_post.author.username
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Url: https://<your-domain>/api/film/<slug>/update
# Headers: Authorization: Token <token>
@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_film(request, slug):
    try:
        film_post = FilmPost.objects.get(slug=slug)
    except FilmPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if film_post.author != user:
        return Response({"msg": "You don't have permission to edit that."})

    if request.method == 'PUT':
        serializer = FilmPostUpdateSerializers(
            film_post, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = UPDATE_SUCCESS
            data['pk'] = film_post.pk
            data['title'] = film_post.title
            data['directors'] = film_post.directors
            data['urlFilm'] = film_post.urlFilm
            data['date_published'] = film_post.date_published
            data['contentFilm'] = film_post.contentFilm
            data['slug'] = film_post.slug
            data['typeFilm'] = film_post.typeFilm
            image_url = str(request.build_absolute_uri(film_post.image.url))
            data['image'] = image_url
            data['author'] = film_post.author.username
            return Response(data=data, status=status.HTTP_200_OK)
        return Response({'status': 'error'}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Url: https://<your-domain>/api/film/<slug>/
# Headers: Authorization: Token <token>
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_film_post_detail(request,slug):
    try:
        film_post = FilmPost.objects.get(slug=slug)
    except FilmPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FilmPostSerializers(film_post)
        return Response(serializer.data)

# Url: https://<your-domain>/api/film/<slug>/delete
# Headers: Authorization: Token <token>
@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def api_film_post_delete(request, slug):
    try:
        film_post = FilmPost.objects.get(slug=slug)
    except FilmPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user = request.user
    if film_post.author != user:
        return Response({"msg":"You don't have permission to delete that."})
    if request.method == 'DELETE':
        operations = film_post.delete()
        data = {}
        if operations:
            data['response'] = DELETE_SUCCESS
        return Response(data=data, status=status.HTTP_200_OK)

# Url: 
#		1) list: https://<your-domain>/api/film/list
#		2) pagination: http://<your-domain>/api/film/list?page=2
#		3) search: http://<your-domain>/api/film/list?search=mitch
#		4) ordering: http://<your-domain>/api/film/list?ordering=-date_updated
#		4) search + pagination + ordering: <your-domain>/api/film/list?search=mitch&page=2&ordering=-date_updated
# Headers: Authorization: Token <token>
class ApiListFilm(ListAPIView):
    queryset = FilmPost.objects.all()
    serializer_class = FilmPostSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title','author__username','directors','typeFilm')
    



    

