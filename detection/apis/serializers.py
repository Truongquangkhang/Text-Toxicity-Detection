# myapp/serializers.py

from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)

class ContentSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=255)
