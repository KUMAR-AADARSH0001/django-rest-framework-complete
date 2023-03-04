from django.db import models

# Create your models here.


class ImageUploder(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField()
