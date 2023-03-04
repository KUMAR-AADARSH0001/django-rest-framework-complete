from django.db.models import fields
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('identity', 'category', 'subcatgeory', 'name', 'amount')
