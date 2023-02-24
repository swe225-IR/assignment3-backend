from django.db import models


# Create your models here.

class Result(models.Model):
    url = models.CharField(max_length=1000)
