from django.contrib import admin

from .models import Car, CarGasData

# Register your models here.

admin.site.register(Car)
admin.site.register(CarGasData)
