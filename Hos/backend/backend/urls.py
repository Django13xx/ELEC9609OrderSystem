"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Add include to the imports here
from rest_framework import routers
from hos import views # add for import the get_image function
from hos.views import (home, CustomerViewSet, MenuViewSet, TableViewSet, OrderViewSet, OrderContentViewSet, PaymentViewSet,CardPayViewSet,
                       auto_dish, order_unpaid, reserve_table, get_order_amount, get_ai_services, pay_bill, show_bill,
                       pay_card, pay_cash, login_check, card_check,get_all_orders, get_total_revenue, logout)

router = routers.DefaultRouter()
router.register('user', CustomerViewSet) # Register the CustomerViewSet with the router and CustomerViewSet will be registered as /api/user
router.register('menu', MenuViewSet) # Register the Menuviewset with the router and MenuViewSet will be registered as /api/menu
router.register('table', TableViewSet) # Register the Tableviewset with the router and TableViewSet will be registered as /api/table
router.register('staff', views.StaffViewSet) # Register the Staffviewset with the router and StaffViewSet will be registered as /api/staff
router.register('order', OrderViewSet) # Register the Orderviewset with the router and OrderViewSet will be registered as /api/order
router.register('orderContent', OrderContentViewSet) # Register the OrderContentViewSet with the router and OrderContentViewSet will be registered as /api/orderContent
router.register('payment', PaymentViewSet) # Register the PaymentViewSet with the router and PaymentViewSet will be registered as /api/payment
router.register('cardpay', CardPayViewSet)  # Register the CardPayViewSet with the router and CardPayViewSet will be registered as /api/cardpay

urlpatterns = [
    path('api/', include(router.urls)),  # basic url for the api
    path('api/function/auto_dish/', auto_dish),  # Determine a unique path for a specific method, auto_dish for generate dish automatically
    path('api/function/order_unpaid/', order_unpaid), # for set the order to unpaid
    path('api/function/reserve_table/', reserve_table), # for reserve table
    path('api/function/get_order_amount/', get_order_amount), # for get the order amount
    path('api/function/ai_services/', get_ai_services), # for get the ai services
    path('api/function/pay_bill/', pay_bill), # for pay the bill
    path('api/function/show_bill/', show_bill), # for show all the bills(payments)
    path('api/function/pay_card/', pay_card), # for pay by card
    path('api/function/pay_cash/', pay_cash), # for pay by cash
    path('api/function/login_check/', login_check), # for admin login check
    path('api/function/card_check/', card_check), # for card check
    path('api/function/get_all_orders/', get_all_orders), # for get all orders
    path('api/function/get_total_revenue/', get_total_revenue), # for get total revenue based on all the successful payments
    path('api/function/logout/', logout), # for admin logout



    path('static/images/<str:image_name>/', views.get_image, name='get_image'), # catch dish name
    path('admin/', admin.site.urls), # django admin functional page
    path('', home, name='home'), # add the url for home
]
