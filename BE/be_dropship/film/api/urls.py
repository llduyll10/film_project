from django.urls import path
from . import views

urlpatterns = [
    path('create', views.api_create_film, name='film-create'),
    path('<slug>/update', views.api_update_film, name='film-update'),
    path('<slug>', views.api_film_post_detail, name='film-detail'),
    path('<slug>/delete', views.api_film_post_delete, name='film-delete'),
    path('list/', views.ApiListFilm.as_view(), name='film-list'),
]