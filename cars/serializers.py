from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    name = serializers.CharField()
    make = serializers.CharField()
    model = serializers.CharField()
    year = serializers.CharField()
