from rest_framework import serializers
from .models import LogMessage


class LogMessageSerializer(serializers.Serializer):
    class Meta:
        model = LogMessage
        fields = ['message', 'log_date']
