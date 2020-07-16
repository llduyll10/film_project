from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core import serializers

from test_nested_relationship.models import Track, Album
from .serializers import AlbumSerializer, TrackSerializer

@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_album(request):
    if request.method == 'POST':
        data = request.data
        serializer = AlbumSerializer(data=data)
        data = {}
        if serializer.is_valid():
            album = serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)