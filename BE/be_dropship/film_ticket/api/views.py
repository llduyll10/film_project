from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core import serializers
from rest_framework.parsers import JSONParser

from film_ticket.models import Chair, Room
from film.models import FilmPost
from .serializers import RoomCreateSerializers, RoomUpdateSerializers


SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_room(request):
    if request.method == 'POST':
        data = request.data
        serializer = RoomCreateSerializers(data=data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
@parser_classes([JSONParser])
def api_detail_room(request, pk):
    if request.method == 'GET':
        room = Room.objects.filter(id=pk).values()
        list_chair = Chair.objects.filter(room=pk).values()
        film_detail = FilmPost.objects.filter(id=room[0]['film_id']).values()
        data = {}
        data['list-chair'] = list_chair
        data['film_detail'] = film_detail
        data['room'] = room
        return Response({'data':data})            

    return Response({'data': 'Error'})

@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_room(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        print('Update room')
        serializer = RoomUpdateSerializers(room, data=request.data, partial=True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = UPDATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
    



    
    

