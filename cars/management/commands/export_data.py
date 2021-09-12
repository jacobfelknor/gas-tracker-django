from cars.models import Car
from django.core.management.base import BaseCommand
from config.settings.utils import get_parameters_aws

FILENAME = "./cars/management/commands/export.txt"
CAR = Car.objects.get(name="Subaru", user=get_parameters_aws("my_gas_tracker_userid"))


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(FILENAME, "w") as file:
            for data in CAR.gas_data.all():
                date = data.date.strftime("%m/%d/%Y")
                print(f"{date}\n{data.cost}\n{data.miles_driven}\n{data.gallons_used}\n{data.mpg}", file=file)
