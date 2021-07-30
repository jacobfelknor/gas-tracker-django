from django.db import models

# Create your models here.


class Car(models.Model):
    user = models.TextField()
    name = models.TextField()
    make = models.TextField()
    model = models.TextField()
    year = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f"{self.name}: {self.year} {self.make} {self.model}"


class CarGasData(models.Model):
    # fk's
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="gas_data")

    # attrs
    # user = models.TextField()
    miles_driven = models.FloatField()
    gallons_used = models.FloatField()
    mpg = models.FloatField()
    cost = models.FloatField()
    date = models.DateField()

    def __str__(self) -> str:
        return f"CarGasData<{self.car}, {self.date}>"
