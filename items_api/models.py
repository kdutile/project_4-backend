from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    description = models.CharField(max_length=280)
    cost = models.IntegerField()
    image = models.CharField(max_length=1000, null=True)
    user = models.CharField(max_length=32, null=True)
