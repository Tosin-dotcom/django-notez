from django.db import models

from django.conf import settings
from notez.storage_backends import PublicMediaStorage

# Create your models here.


class Category(models.Model):
    sector = models.CharField(max_length=100)
    #image1 = models.ImageField(upload_to="uploads/")
    #image2 = models.ImageField(upload_to="uploads/")
    #image3 = models.ImageField(upload_to="uploads/")
    image1 = models.ImageField(
        storage=PublicMediaStorage(), upload_to="uploads/")
    image2 = models.ImageField(
        storage=PublicMediaStorage(), upload_to="uploads/")
    image3 = models.ImageField(
        storage=PublicMediaStorage(), upload_to="uploads/")

    def __str__(self):
        return self.sector


class Note(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    last = models.DateTimeField(auto_now=True)
    name = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title[:10]}..."
