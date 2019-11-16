from django.db import models

# Create your models here.
class Slideshow(models.Model):
    title = models.CharField(max_length=100)
    slides = models.TextField()