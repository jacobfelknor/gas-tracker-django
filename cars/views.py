from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework.views import APIView

from .models import Car
from .serializers import CarGasDataSerializer, CarSerializer

# Create your views here.


class GetCars(APIView):
    def post(self, request: HttpRequest) -> JsonResponse:
        raise NotImplementedError

    def get(self, request: HttpRequest) -> JsonResponse:
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        data = serializer.data
        # serialized stuff here
        return JsonResponse(data, safe=False)


class GetCarGasData(APIView):
    def get(self, request: HttpRequest, id: str) -> JsonResponse:
        car_data = Car.objects.get(pk=id).gas_data.all()
        serializer = CarGasDataSerializer(car_data, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)
