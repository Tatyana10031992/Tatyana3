from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_lyrics, {'lang': 'en'}, name='song_lyrics_en'),
    path('fr/', views.song_lyrics, {'lang': 'fr'}, name='song_lyrics_fr'),
    path('de/', views.song_lyrics, {'lang': 'de'}, name='song_lyrics_de'),
    path('es/', views.song_lyrics, {'lang': 'es'}, name='song_lyrics_es'),
]

