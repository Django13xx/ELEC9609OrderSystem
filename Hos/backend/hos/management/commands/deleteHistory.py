import csv
from django.core.management.base import BaseCommand
from hos.models import Order, OrderContent, Payment, Customer  # import the model

class Command(BaseCommand):

    def handle(self, *args, **options):

        # delete all the records existed in the model
        Order.objects.all().delete()
        OrderContent.objects.all().delete()
        Payment.objects.all().delete()
        Customer.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Delete all data in Order, Ordercontent, Payment and Customer successfully'))