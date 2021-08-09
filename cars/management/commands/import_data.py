from cars.models import Car, CarGasData
from dateutil import parser as dt_parser
from django.core.management.base import BaseCommand
from config.settings.keys import me

FILENAME = "./cars/management/commands/subData.txt"
CAR = Car.objects.get(name="Subaru", user=me)


def chunks(l, n):
    n = max(1, n)
    return (l[i : i + n] for i in range(0, len(l), n))


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(FILENAME, "r") as file:
            lines = [x.strip() for x in file.readlines()]
            groups = chunks(lines, 5)

            for group in groups:
                new_gas_data = CarGasData(
                    car=CAR,
                    date=dt_parser.parse(group[0]).date(),
                    cost=float(group[1]),
                    miles_driven=float(group[2]),
                    gallons_used=float(group[3]),
                    mpg=float(group[4]),
                )
                new_gas_data.save()
