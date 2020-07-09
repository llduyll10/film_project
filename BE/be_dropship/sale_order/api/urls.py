from django.urls import path
from . import views

urlpatterns = [
    path('create', views.api_create_show_time, name='show-time-create'),
]