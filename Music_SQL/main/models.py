from django.db import models


class Artists(models.Model):
    name = models.CharField(max_length=128)
    date_of_start = models.DateField()
    date_of_end = models.DateField()
# Create your models here.
