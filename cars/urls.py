from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('toyota/', views.car_brand, {'brand': 'toyota'}, name='toyota'),
    path('honda/', views.car_brand, {'brand': 'honda'}, name='honda'),
    path('renault/', views.car_brand, {'brand': 'renault'}, name='renault'),
]
