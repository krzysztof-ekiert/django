from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.IntegerField(max_length=4)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title