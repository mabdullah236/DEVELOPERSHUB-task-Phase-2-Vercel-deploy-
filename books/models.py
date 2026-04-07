from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    isbn = models.CharField(unique=True, max_length=13)
    publishedDate = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True, blank=True)

    def __str__(self):
        return self.title