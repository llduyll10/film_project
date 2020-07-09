from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registration_view, name='register'),
    path('login', views.ObtainAuthTokenView.as_view(), name='login'),
    path('profile/update', views.update_account_view, name='update')
]