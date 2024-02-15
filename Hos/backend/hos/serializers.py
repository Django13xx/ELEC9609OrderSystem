from rest_framework import serializers
from .models import Customer, Menu, Table, Staff, Order, OrderContent, Payment, CardPay

# Serializers define the API representation.

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderContent
        fields = '__all__'

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CardPaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardPay
        fields = '__all__'