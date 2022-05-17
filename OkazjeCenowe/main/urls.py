
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('znalezione/', views.wyszukanie, name='wyszukiwanie'),
    path('zapisz_nowe/', views.dodaj, name='dodaj')
    
]

