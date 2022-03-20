from rest_framework import serializers
from .models import Item

class ItemSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'description', 'cost', 'image',)
