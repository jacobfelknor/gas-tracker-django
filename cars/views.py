from dateutil import parser as dt_parser
from django.core.exceptions import PermissionDenied

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework.views import APIView

from .models import Car, CarGasData
from .serializers import CarGasDataSerializer, CarSerializer

# Create your views here.


class GetCars(APIView):
    def post(self, request: HttpRequest) -> JsonResponse:
        raise NotImplementedError

    def get(self, request: HttpRequest, user: str) -> JsonResponse:
        cars = Car.objects.filter(user=user)
        serializer = CarSerializer(cars, many=True)
        data = serializer.data
        # serialized stuff here
        return JsonResponse(data, safe=False)


class AddCar(APIView):
    def post(self, request: HttpRequest, user: str) -> JsonResponse:
        data: dict = request.data
        name = data.get("name")
        make = data.get("make")
        model = data.get("model")
        year = int(data.get("year"))
        new_car = Car(user=user, name=name, make=make, model=model, year=year)
        new_car.save()
        return JsonResponse(CarSerializer(new_car).data)

    def get(self, request: HttpRequest) -> JsonResponse:
        raise NotImplementedError


class CarGasDataAPI(APIView):
    def get(self, request: HttpRequest, user: str, id: str) -> JsonResponse:
        car = Car.objects.get(id=id)
        if car.user != user:
            raise PermissionDenied
        car_data = CarGasData.objects.filter(car_id=id).order_by("-date")
        serializer = CarGasDataSerializer(car_data, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    def post(self, request: HttpRequest, user: str, id: str) -> JsonResponse:
        data: dict = request.data
        car = Car.objects.get(id=id)
        if car.user != user:
            raise PermissionDenied
        miles_driven = float(data.get("miles_driven"))
        gallons_used = float(data.get("gallons_used"))
        cost = float(data.get("cost"))
        mpg = miles_driven / gallons_used
        date = dt_parser.parse(data.get("date")).date()

        new_gas_data = CarGasData(
            car=car,
            miles_driven=miles_driven,
            gallons_used=gallons_used,
            cost=cost,
            mpg=mpg,
            date=date,
        )
        new_gas_data.save()

        return JsonResponse(CarGasDataSerializer(new_gas_data).data)
