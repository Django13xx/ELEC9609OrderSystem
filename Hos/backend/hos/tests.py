from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer, Menu, Table, Staff, Order, OrderContent, Payment, CardPay
from .serializers import CustomerSerializer, MenuSerializer, TableSerializer, StaffSerializer, OrderSerializer, OrderContentSerializer, PaymentSerializer, CardPaySerializer


class ModelTestCase(TestCase):
    def setUp(self):
        # Create some sample data for testing
        self.customer = Customer.objects.create(customer_id=1, customer_phone="123-456-7890")
        self.staff = Staff.objects.create(staff_id=1, staff_password="password", staff_name="John Doe",
                                          staff_phone="987-654-3210", staff_email="john@example.com")
        self.menu_item = Menu.objects.create(dish_id=1, dish_name="Spaghetti", dish_type="Pasta",
                                             dish_price=12.99, dish_qty=10)
        self.table = Table.objects.create(table_id=1, table_name="Table 1", table_capacity=4, table_status=True)
        self.order = Order.objects.create(order_id=1, order_code="ORDER123", order_table=1,
                                          order_numberOfPeople=4, order_total_amount=30.00, order_status="order created")
        self.order_content = OrderContent.objects.create(order=self.order, dish_name="Spaghetti", dish_qty=2)
        self.payment = Payment.objects.create(payment_id=1, payment_order="ORDER123", payment_time="2023-10-30T12:00:00Z",
                                             payment_method="Credit Card", payment_amount=30.00)

    def test_customer_model(self):
        customer = Customer.objects.get(customer_id=1)
        self.assertEqual(customer.customer_phone, "123-456-7890")

    def test_staff_model(self):
        staff = Staff.objects.get(staff_id=1)
        self.assertEqual(staff.staff_name, "John Doe")

    def test_menu_model(self):
        menu_item = Menu.objects.get(dish_id=1)
        self.assertEqual(menu_item.dish_name, "Spaghetti")

    def test_table_model(self):
        table = Table.objects.get(table_id=1)
        self.assertEqual(table.table_name, "Table 1")

    def test_order_model(self):
        order = Order.objects.get(order_id=1)
        self.assertEqual(order.order_code, "ORDER123")

    def test_order_content_model(self):
        order_content = OrderContent.objects.get(dish_name="Spaghetti")
        self.assertEqual(order_content.dish_qty, 2)

    def test_payment_model(self):
        payment = Payment.objects.get(payment_id=1)
        self.assertEqual(payment.payment_method, "Credit Card")

    def test_get_image_view(self):
        response = self.client.get('/static/images/Beef.jpg/')
        self.assertEqual(response.status_code, 200)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {'customer_id': 1, 'customer_phone': '123-456-7890'}
        self.staff_data = {'staff_id': 1, 'staff_password': 'password', 'staff_name': 'John Doe',
                           'staff_phone': '987-654-3210', 'staff_email': 'john@example.com', 'staff_status': True}
        self.menu_data = {'dish_id': 1, 'dish_name': 'Spaghetti', 'dish_type': 'Pasta',
                          'dish_price': 12.99, 'dish_qty': 10}
        self.table_data = {'table_id': 1, 'table_name': 'Table 1', 'table_capacity': 4, 'table_status': True}
        self.order_data = {'order_id': 1, 'order_code': 'ORDER123', 'order_table': 1,
                           'order_numberOfPeople': 4, 'order_total_amount': 30.00, 'order_status': 'order created'}
        self.order_content_data = {'order': 'ORDER123', 'dish_name': 'Spaghetti', 'dish_qty': 2}
        self.payment_data = {'payment_id': 1, 'payment_order': 'ORDER123', 'payment_time': '2023-10-30T12:00:00Z',
                             'payment_method': 'Credit Card', 'payment_amount': 30.00}
        self.card_pay_data = {'cardholder_name': 'John Doe', 'card_number': '1234567890123456',
                              'expire_date': '12/25', 'cvv_number': '123'}
        self.image_name = 'Beef.jpg'

    def test_get_customer(self):
        response = self.client.get(reverse('customer-list'))
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_menu(self):
        response = self.client.get(reverse('menu-list'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_table(self):
        response = self.client.get(reverse('table-list'))
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_staff(self):
        response = self.client.get(reverse('staff-list'))
        staff_members = Staff.objects.all()
        serializer = StaffSerializer(staff_members, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_order(self):
        response = self.client.get(reverse('order-list'))
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_order_content(self):
        response = self.client.get(reverse('ordercontent-list'))
        order_contents = OrderContent.objects.all()
        serializer = OrderContentSerializer(order_contents, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_payment(self):
        response = self.client.get(reverse('payment-list'))
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_card_pay(self):
        response = self.client.get(reverse('cardpay-list'))
        card_payments = CardPay.objects.all()
        serializer = CardPaySerializer(card_payments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_image(self):
        response = self.client.get(reverse('get_image', args=[self.image_name]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# More test cases will be created here.
