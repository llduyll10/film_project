from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from sale_order.models import ShowTimePost, ChairPost
from .serializers import ShowTimePostCreateSerializers, ChairPostSerializers

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Url: https://<your-domain>/api/show-time/create
# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_show_time(request):
    if request.method == 'POST':
        data = request.data
        serializer = ShowTimePostCreateSerializers(data=data)
        amount_chair= request.data['amount_chair']
        #Create list chair

        chair = ChairPost.objects.create(type_chair=False, status=False, price=75000.00)
        for _ in range (amount_chair + 1):
            list_chair = [chair] * amount_chair
         
        # chair_serializer = ChairPostSerializers(data=chair)
        # if chair_serializer.is_valid():
        #     chair_serializer.save()
        #     list_chair = [chair_serializer] * amount_chair

        
        print(list_chair[0])
        data = {}
        return Response({'status':'ok'})




