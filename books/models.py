from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    available = models.BooleanField(default=True)

    def _str_(self):
        return self.title
    

class UserLogin(models.Model):
    name = models.CharField(max_length=100)  # Field for storing the user's name
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=128)  # Store hashed passwords instead of plain text
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.email})"