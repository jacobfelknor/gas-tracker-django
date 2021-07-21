from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    make = serializers.CharField()
    model = serializers.CharField()
    year = serializers.CharField()
    pprint = serializers.SerializerMethodField()

    def get_pprint(self, object):
        return str(object)


class CarGasDataSerializer(serializers.Serializer):
    miles_driven = serializers.FloatField()
    gallons_used = serializers.FloatField()
    mpg = serializers.FloatField()
    cost = serializers.FloatField()
    date = serializers.DateField()
