from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    created_date = models.DateTimeField(auto_now_add=True)
