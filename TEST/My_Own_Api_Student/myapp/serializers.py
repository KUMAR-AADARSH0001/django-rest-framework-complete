from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'gender', 'school', 'join_standard', 'pass_standard', 'favourite_miss', 'pass_or_not',
                  'passby', 'relation_type', 'describe_yourself', 'created_at', 'updated_at']
