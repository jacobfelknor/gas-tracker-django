from django.db import models

# Create your models here.


class Car(models.Model):
    # id: number;
    # name: string;
    # make: string;
    # model: string;
    # year: string;

    name = models.TextField()
    make = models.TextField()
    model = models.TextField()
    year = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f"{self.name}: {self.year} {self.make} {self.model}"