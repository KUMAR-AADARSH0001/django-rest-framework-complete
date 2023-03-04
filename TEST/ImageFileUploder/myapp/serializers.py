from rest_framework import serializers
from .models import ImageUploder


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploder
        fields = ['id', 'name', 'address', 'image']
