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
        list_chair = []
        for _ in range(amount_chair + 1):
            data_chair = {'type_chair':False,'price':75000.00, 'status':False}
            chair_serializer = ChairPostSerializers(data=data_chair)
            if chair_serializer.is_valid():
                chair_serializer.save()
                list_chair.append(chair_serializer)


       
         
        # chair_serializer = ChairPostSerializers(data=chair)
        # if chair_serializer.is_valid():
        #     chair_serializer.save()
        #     list_chair = [chair_serializer] * amount_chair

        
        print(list_chair)
        data = {}
        return Response({'status':'ok'})




