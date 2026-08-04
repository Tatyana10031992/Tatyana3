from django.urls import path
from . import views

app_name = 'starwars_app'

urlpatterns = [
    path('', views.starwars_home, name='home'),
    path('films/', views.films_list, name='films_list'),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path('people/', views.people_list, name='people_list'),
    path('people/<int:person_id>/', views.person_detail, name='person_detail'),
    path('planets/', views.planets_list, name='planets_list'),
    path('planets/<int:planet_id>/', views.planet_detail, name='planet_detail'),
    path('starships/', views.starships_list, name='starships_list'),
    path('starships/<int:starship_id>/', views.starship_detail, name='starship_detail'),
]