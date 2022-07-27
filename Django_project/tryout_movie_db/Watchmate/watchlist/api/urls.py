from django.urls import path, include
from watchlist.api.views import movie_list, movie_details
from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>', movie_details, name='movie-detail'),
    path("get-details", UserDetailAPI.as_view()),
    path('register', RegisterUserAPIView.as_view()),
]
