from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('clients/', views.clients, name='clients'),
    path('waiters/', views.waiters, name='waiters'),
    path('orders/', views.orders, name='orders'),
    path('locations/', views.locations, name='locations'),
    path('ordercards/', views.order_card, name='ordercards'),
]