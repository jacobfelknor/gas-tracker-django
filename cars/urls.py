from django.urls import path

from . import views

app_name = "cars"

urlpatterns = [
    path("get_cars/<user>", views.GetCars.as_view(), name="get_cars"),
    path("car_data/<user>/<id>", views.CarGasDataAPI.as_view(), name="car_data"),
    path("add_car/<user>", views.AddCar.as_view(), name="add_car"),
]
