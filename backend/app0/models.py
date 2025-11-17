from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.CharField(max_length=100, default="")
    price = models.FloatField(default=0.)
