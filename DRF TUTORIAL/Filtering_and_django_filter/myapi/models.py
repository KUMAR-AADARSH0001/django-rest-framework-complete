from django.db import models
import datetime
YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year+1)]

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    year = models.IntegerField(
        ('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
