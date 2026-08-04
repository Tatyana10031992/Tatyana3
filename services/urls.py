from django.urls import path
from . import views

urlpatterns = [
   path('fortune/', views.fortune, name='fortune'),
    
   
    path('random/number/', views.random_single, name='random_single'),
    path('random/range/<int:min_val>/<int:max_val>/', views.random_range, name='random_range'),
    path('random/list/<int:count>/', views.random_list, name='random_list'),

    path('poems/', views.poem_random, name='poem_random'),
    path('poems/author/<str:author>/', views.poem_by_author, name='poem_by_author'),
    path('poems/theme/<str:theme>/', views.poem_by_theme, name='poem_by_theme'),
    
    path('poems/authors/', views.list_authors, name='list_authors'),
    path('poems/themes/', views.list_themes, name='list_themes'),
    path('poems/titles-by-theme/<str:theme>/', views.titles_by_theme, name='titles_by_theme'),
]
