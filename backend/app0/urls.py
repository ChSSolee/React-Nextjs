from django.urls import path, include
from .views import create_book

urlpatterns = [
    path('create/', create_book, name='create_book'),
]