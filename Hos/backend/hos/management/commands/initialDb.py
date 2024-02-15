import csv
from django.core.management.base import BaseCommand
from hos.models import Menu, Staff, Table, CardPay # import the model

class Command(BaseCommand):
    help = 'Load menu data from CSV file'

    def handle(self, *args, **options):

        # initial menu database----------------------------------------------------------------
        csv_file_path = 'static/menu.csv'  # csv file path relative to manage.py

        # delete all the records existed in the model
        Menu.objects.all().delete()

        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                dish_id,dish_name, dish_type, dish_price, dish_qty = row
                # create or update the record
                Menu.objects.create(
                    dish_id=dish_id,
                    dish_name=dish_name,
                    dish_type=dish_type,
                    dish_price=dish_price,
                    dish_qty=dish_qty,
                )

        self.stdout.write(self.style.SUCCESS('Menu data loaded successfully'))


        #initial staff database----------------------------------------------------------------
        csv_file_path_2 = 'static/staffDetail.csv'  # csv file path relative to manage.py

        # delete all the records existed in the model
        Staff.objects.all().delete()

        with open(csv_file_path_2, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                staff_id, staff_password, staff_name, staff_phone, staff_email = row
                # create or update the record
                Staff.objects.create(
                    staff_id=staff_id,
                    staff_password=staff_password,
                    staff_name=staff_name,
                    staff_phone=staff_phone,    
                    staff_email=staff_email,
                )
                
        self.stdout.write(self.style.SUCCESS('Staff data loaded successfully'))


        # initial table database----------------------------------------------------------------
        csv_file_path_3 = 'static/table.csv'  # csv file path relative to manage.py

        # delete all the records existed in the model
        Table.objects.all().delete()

        with open(csv_file_path_3, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                table_id, table_name, table_capacity, table_status = row
                # create or update the record
                Table.objects.create(
                    table_id=table_id,
                    table_name=table_name,
                    table_status=table_status,
                    table_capacity=table_capacity,
                )

        self.stdout.write(self.style.SUCCESS('Table data loaded successfully'))


        # initial card database----------------------------------------------------------------
        csv_file_path_4 = 'static/cardpay.csv' # Get file path
        
        # delete all the records existed in the model
        CardPay.objects.all().delete()

        with open(csv_file_path_4, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header of the first line of the csv file
            for row in reader:  # Assigns a value to consecutive items in a row
                 id, cardholder_name,card_number,expire_date,cvv_number= row
                 # creat or update the record
                 CardPay.objects.create(
                      id=id,
                      cardholder_name=cardholder_name,
                      card_number=card_number,
                      expire_date=expire_date,
                      cvv_number=cvv_number,
                 )
   
        self.stdout.write(self.style.SUCCESS('Card data loaded successfully'))
