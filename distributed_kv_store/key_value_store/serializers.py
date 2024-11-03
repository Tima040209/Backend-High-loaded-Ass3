from rest_framework import serializers

class KeyValueSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=100)
    value = serializers.CharField(max_length=1000)
