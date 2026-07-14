from django.urls import path
from . import views

urlpatterns = [
    path('', views.prog_day_view, name='prog_day'),
]
