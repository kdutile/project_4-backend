from django.db import models
from auth_api.models import UserAccount

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    description = models.CharField(max_length=280)
    cost = models.IntegerField()
    image = models.CharField(max_length=1000, null=True)
    user = models.ForeignKey(UserAccount, related_name='items', null=True, on_delete=models.CASCADE)
