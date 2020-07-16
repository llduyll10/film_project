from django.urls import path
from . import views

urlpatterns = [
    path('room/create', views.api_create_room, name='room-create'),
    path('room/<int:pk>', views.api_detail_room, name='room-detail'),
    path('room/update/<int:pk>',views.api_update_room, name='room-update')
]