from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    description = models.CharField(max_length=280)
    cost = models.IntegerField()
