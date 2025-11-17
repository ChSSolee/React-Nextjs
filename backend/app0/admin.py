from django.contrib import admin
from .models import Book   # app0 안에 있는 모델

admin.site.register(Book)
