from django.db import models
import datetime
# Create your models here.


class Student(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))
    GENDER_CHOICE = [('M', 'MALE'), ('F', 'FEMALE'), ('T', 'TRANCE')]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    school = models.CharField(max_length=100)
    join_standard = models.CharField(max_length=100)
    pass_standard = models.CharField(max_length=100)
    favourite_miss = models.CharField(max_length=100)
    pass_or_not = models.BooleanField()
    passby_class = models.CharField(max_length=100)
    passing_parsent = models.IntegerField()
    passby = models.IntegerField(('passby'), choices=YEAR_CHOICES,
                                 default=datetime.datetime.now().year)
    relation_type = models.CharField(max_length=100)
    describe_yourself = models.CharField(max_length=999999)
    created_at = models.DateTimeField(
        null=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now_add=True)
