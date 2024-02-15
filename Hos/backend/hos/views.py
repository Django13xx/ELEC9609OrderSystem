from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, MenuSerializer, TableSerializer, StaffSerializer, OrderSerializer, OrderContentSerializer, PaymentSerializer,CardPaySerializer
# import the following for auto_dish function
from django.http import JsonResponse
from hos.models import Customer, Menu, Table, Staff, Order, OrderContent, Payment, CardPay
# import the following for get_image function
from django.http import HttpResponse
from django.conf import settings
import os
import random
from collections import Counter
from decouple import config
import requests
import openai
from datetime import datetime # add for pay_cash function

from django.db.models import F # add for update_menu function

SERVICE_PROMPT_HEADER = ("I am currently in a hotpot restaurant and ordering food."\
                         "The dishes in the restaurant menu are listed below:" +
                         "Beef, Lamb, Chicken, Pork, Fish, Prawn, Crab, Fish fillet," +
                         "Fish balls, Scallops, Tofu, Mushrooms, Spinach, Bean sprouts," +
                         "Leeks, Tofu skin, Vermicelli noodles, Rice noodles, Udon, Sliced beef," +
                         "Chicken balls, Lamb skewers and Pork belly.")


# Create all views here for all the models respectively.
def home(request):
    # You can add any additional context data you want to pass to the template here
    context = {
        'page_title': 'Welcome to Our Website',
        'welcome_message': 'Hello, and welcome to our website!',
    }
    return render(request, 'home.html', context)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('customer_id')
    serializer_class = CustomerSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('dish_id')
    serializer_class = MenuSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('table_id')
    serializer_class = TableSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('staff_id')
    serializer_class = StaffSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_id')
    serializer_class = OrderSerializer


class OrderContentViewSet(viewsets.ModelViewSet):
    queryset = OrderContent.objects.all().order_by('id')
    serializer_class = OrderContentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('payment_id')
    serializer_class = PaymentSerializer


class CardPayViewSet(viewsets.ModelViewSet):
    queryset = CardPay.objects.all().order_by('cardholder_name')
    serializer_class = CardPaySerializer


# Add the following function for get the image
def get_image(request, image_name):
    image_path = os.path.join(settings.STATIC_ROOT, 'images', image_name)
    with open(image_path, 'rb') as image_file:
        return HttpResponse(image_file.read(), content_type='image/jpg')


# Auto Dish System: gereate the dish for customer
def auto_dish(request):
    people_number = int(request.GET.get('people_number', 1))
    # Genrate the number of each type of dish
    maincourse_number = people_number // 2 + 1
    seafood_number = people_number // 2
    vegetarian_number = people_number // 2
    noodles_number = people_number // 3
    meat_number = people_number // 3 + 1

    # AI algorithm to generate the dish
    main_course = Menu.objects.filter(dish_type="MainCourse")
    seafood = Menu.objects.filter(dish_type="Seafood")
    vegetarian = Menu.objects.filter(dish_type="Vegetarian")
    noodles = Menu.objects.filter(dish_type="Noodles")
    meat = Menu.objects.filter(dish_type="Meat")

    random_menu = random.choices(list(main_course), k=maincourse_number)
    random_menu.extend(random.choices(list(seafood), k=seafood_number))
    random_menu.extend(random.choices(list(meat), k=meat_number))
    random_menu.extend(random.choices(list(vegetarian), k=vegetarian_number))
    random_menu.extend(random.choices(list(noodles), k=noodles_number))
    # After generating random_menu
    dish_names = [dish.dish_name for dish in random_menu]
    dishes_count = dict(Counter(dish_names))
    # return the dish to frontend
    response_data = [{'dish_name': dish_name, 'dish_qty': str(dish_qty)} for dish_name, dish_qty in
                     dishes_count.items()]

    return JsonResponse(response_data, safe=False)


# Create an unpaid order for customer when start order (login)
def order_unpaid(request):
    order_code = request.GET.get('order_code', 1)
    order_amount = request.GET.get('total_amount', 1)
    print('order:'+order_code+ 'amount:'+str(order_amount))
    orders = Order.objects.filter(order_code=order_code)
    for order in orders:
        order.order_total_amount = order_amount
        order.order_status = 'order unpaid'
        order.save()
    print('hello')
    return JsonResponse({'order_amount': order_amount}, safe=False)


# Reserve the table for customer when start order (login)
def reserve_table(request):
    table_name = request.GET.get('table_name', 1)
    table = Table.objects.get(table_name=table_name)
    table.table_status = False
    table.save()
    return JsonResponse({'table_status': table.table_status}, safe=False)


# Get the order amount for a specific order code
def get_order_amount(request):
    order_code = request.GET.get('order_code', 1)
    orders = Order.objects.filter(order_code=order_code)
    for order in orders:
        print(order.order_total_amount)
        order_amount = order.order_total_amount
    return JsonResponse({'order_amount': order_amount}, safe=False)


# Get ai services through the openai api
def get_ai_services(request):
    statement = str(request.GET.get('statement', "Please give me some recommendations."))
    prompt = SERVICE_PROMPT_HEADER + statement
    response = query_gpt(prompt)
    return JsonResponse({'message': response['choices'][0]['text'].encode('utf-8').decode('utf-8')})


# Query gpt in the function of get_ai_services
def query_gpt(prompt):
    # openai_api_key = config('OPENAI_API_KEY')
    # headers = {
    #     'Authorization': f'Bearer {openai_api_key}',
    #     'Content-Type': 'application/json',
    # }
    # data = {
    #     'prompt': prompt,
    #     'max_tokens': 300,
    # }
    # response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, json=data)
    # if response.status_code == 200:
    #     response_data = response.json()  # Parse the JSON content of the response
    #     return response_data
    # else:
    #     print(f"Request failed with status code {response.status_code}.")
    #     return None
    openai.api_key = config("OPENAI_API_KEY")
    return openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=300,
        temperature=0
    )


# Pay the bill once the customer reach the payment page
def pay_bill(request):
    order_code = request.GET.get('order_code', 1)
    orders = Order.objects.filter(order_code=order_code)
    for order in orders:
        order.order_status = 'order paid'
        order.save()
    return JsonResponse({'order_amount': order.order_total_amount}, safe=False)


# Show all the order details as the bill contents by order code provided
def show_bill(request):
    order_code = request.GET.get('order_code', 1)
    ordercontents = OrderContent.objects.filter(order=order_code)
    response_data = []
    for order in ordercontents:
        dish_name = order.dish_name
        dish_qty = order.dish_qty
        dish_price = Menu.objects.get(dish_name=dish_name).dish_price * dish_qty
        print("dish_name: " + str(dish_name) + " dish_qty: " + str(dish_qty) + " dish_price: " + str(dish_price))

        response_data.append({"dish_name": str(dish_name), "dish_qty": str(dish_qty), "dish_price": str(dish_price)})
    return JsonResponse(response_data, safe=False)


# Call this function to set the payment status to "Card" when customer choose to pay by card
def pay_card(request):
    order_code = request.GET.get('order_code', 1)
    update_menu(order_code)
    empty_table(order_code)
    orders = Order.objects.filter(order_code=order_code)
    for order in orders:
        payment_amount = order.order_total_amount
        payment_time = datetime.now()
        payment_method = 'Card'
        payment_order = order_code
        Payment.objects.create(payment_amount=payment_amount,
                               payment_time=payment_time,
                               payment_method=payment_method,
                               payment_order=payment_order)
    return JsonResponse({'message': payment_method}, safe=False)


# Call this function to set the payment status to "Cash" when customer choose to pay by card
def pay_cash(request):
    order_code = request.GET.get('order_code', 1)
    update_menu(order_code)
    empty_table(order_code)
    orders = Order.objects.filter(order_code = order_code)
    for order in orders:
        payment_amount = order.order_total_amount
        payment_time = datetime.now()
        payment_method = 'Cash'
        payment_order = order_code
        Payment.objects.create(payment_amount=payment_amount,
                               payment_time=payment_time,
                               payment_method=payment_method,
                               payment_order=payment_order)
    return JsonResponse({'message': payment_method}, safe=False)


# Update the order content after the customer order successfully
def update_menu(order_code):
    ordercontents = OrderContent.objects.filter(order = order_code)
    for ordercontent in ordercontents:
        Menu.objects.filter(dish_name = ordercontent.dish_name).update(dish_qty=F('dish_qty') + ordercontent.dish_qty)


# Empty the table after the customer pay the bill
def empty_table(order_code):
    orders = Order.objects.filter(order_code = order_code)
    for order in orders:
        table_name = order.order_table
        Table.objects.filter(table_name = table_name).update(table_status=True)


# Check the validity of the admin login
def login_check(request):
    if 'name' in request.GET and 'password' in request.GET:
        name = request.GET['name']
        password = request.GET['password']
        staff = Staff.objects.filter(staff_id=name, staff_password=password)
        if staff:
            staff.update(staff_status=True)
            return JsonResponse(True, safe=False)
    return JsonResponse(False, safe=False)


# Check the validity of the card
def card_check(request):
    if 'name' in request.GET and 'number' in request.GET and 'date'in request.GET and 'cvv' in request.GET:
        name = request.GET['name']
        number = request.GET['number']
        date = request.GET['date']
        cvv = request.GET['cvv']
        cardpay = CardPay.objects.filter(cardholder_name=name,card_number=number,expire_date=date,cvv_number=cvv)
        if cardpay:
            return JsonResponse(True, safe=False)
    return JsonResponse(False, safe=False)
        

# Get all the order details for the admin
def get_all_orders(request):
    orders = Order.objects.all()
    order_contents = OrderContent.objects.all()
    order_dict = {}
    for order_content in order_contents:
        order_id = order_content.order
        for order in orders:
            if order.order_code == order_id and order.order_status == "order paid":
                if order_content.dish_name in order_dict:
                    order_dict[order_content.dish_name] += order_content.dish_qty
                else:
                    order_dict[order_content.dish_name] = order_content.dish_qty
    response_data = [{'dish_name': dish_name, 'dish_qty': str(dish_qty)} for dish_name, dish_qty in
                     order_dict.items()]
    return JsonResponse(response_data, safe=False)


# Get the total revenue for the admin
def get_total_revenue(request):
    payments = Payment.objects.all()
    total_revenue = 0
    for payment in payments:
        total_revenue += payment.payment_amount
    return JsonResponse({'totalRevenue': "$ "+str(total_revenue)})


# Admin logout
def logout(request):
    if 'admin' in request.GET:
        admin = request.GET['admin']
        staff = Staff.objects.filter(staff_id=admin)
        if staff:
            staff.update(staff_status=False)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})
