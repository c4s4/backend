from django.urls import path

from . import views

urlpatterns = [
    path('customer/<int:id>', views.customer, name='customer'),
    path('customer/since/<time>', views.customer_since, name='customer-since'),
    path('customer/create', views.customer_create, name='customers-create'),
]
