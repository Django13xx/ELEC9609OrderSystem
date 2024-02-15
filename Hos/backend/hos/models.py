from django.db import models
from django.http import HttpResponse


# Create all models here including customer, staff, menu...
# Customer Table
class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_phone = models.CharField(max_length=50)


# Staff Login Table
class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    staff_password = models.CharField(max_length=100)
    staff_name = models.CharField(max_length=100)
    staff_phone = models.CharField(max_length=50)
    staff_email = models.CharField(max_length=50)
    staff_status = models.BooleanField(default=False)


# Menu Table
class Menu(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=100)
    dish_type = models.CharField(max_length=50)
    dish_price = models.FloatField()
    dish_qty = models.IntegerField(default=0) # this is the quantity of the dish sold


# Get image function for dishes in frontend
def get_image(request, image_name):
    image = Menu.objects.get(dish_pic=image_name)
    return HttpResponse(image, content_type='image/jpg')


# Table Table
class Table(models.Model):
    table_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=50, default="")
    table_capacity = models.IntegerField()
    table_status = models.BooleanField(default=False)


# Order Table
class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_code = models.CharField(max_length=50, default="")
    order_table = models.IntegerField()
    order_numberOfPeople = models.IntegerField()
    order_total_amount = models.FloatField(default=0)
    order_status = models.CharField(default="order created", max_length=50)


# Order Contents Table
class OrderContent(models.Model):
    order = models.CharField(max_length=100)
    dish_name = models.CharField(max_length=100)
    dish_qty = models.IntegerField()


# Payment Table
class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    payment_order = models.CharField(max_length=100)
    payment_time = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    payment_amount = models.FloatField()


# Card Pay Table
class CardPay(models.Model):
    cardholder_name = models.CharField(max_length=100) 
    card_number = models.CharField(max_length=20) 
    expire_date = models.CharField(max_length=20) 
    cvv_number = models.CharField(max_length=20) 

