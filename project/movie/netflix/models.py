from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

def __str__(self):
    return self.name

class movies(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    year = models.DateField()
    poster = models.ImageField(upload_to="movie/posters")
    video = models.FileField(upload_to="movie/video")
    categories = models.ManyToManyField(Category)