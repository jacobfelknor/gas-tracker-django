from django.urls import path

from . import views

app_name = "cars"

urlpatterns = [
    path("get_cars/", views.GetCars.as_view(), name="get_cars"),
]
