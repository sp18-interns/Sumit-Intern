from django.urls import path
from .views import restaurant_list
from . import views

urlpatterns = [
    path('restaurants/', views.Restaurants.as_view()),
    path('restaurants/<str:restaurant_id>/', views.RestaurantDetail.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/', views.Recipes.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/', views.RecipeDetail.as_view()),
    path('restaurants/list/', restaurant_list, name='restaurants_list'),
]
