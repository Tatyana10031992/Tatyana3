from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc_view, name='calc'),
]
