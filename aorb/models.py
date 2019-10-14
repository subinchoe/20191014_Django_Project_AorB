from django.db import models

# Create your models here.
class Question(models.Model):
    ask = models.CharField(max_length=50)
    itemA = models.CharField(max_length=50)
    itemB = models.CharField(max_length=50)


