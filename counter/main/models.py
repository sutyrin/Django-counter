from django.db import models

# Create your models here.
class Counter(models.Model):
    value = models.IntegerField()
