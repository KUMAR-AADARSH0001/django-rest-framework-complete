from django.db import models
import random


class Item(models.Model):
    identity = models.CharField(max_length=100)
    category = models.CharField(max_length=255)
    subcatgeory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
