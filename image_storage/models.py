from django.db import models

# Create your models here.

class Image(models.Model):
    link = models.CharField(max_length=1024)
    graphics = models.ImageField()