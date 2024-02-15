from django.contrib import admin
from .models import *
# Register models here that can be access through admin mode.
register_models = [Customer, Staff, Menu, Table, Order, OrderContent]
admin.site.register(register_models)