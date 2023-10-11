# person/urls.py
from django.urls import path
from .views import add, show

urlpatterns = [
    path('', show, name='show'),
    path('add/', add, name='add'),
]
