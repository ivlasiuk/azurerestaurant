from django.contrib import admin
from .models import Client, Waiter, Order, Location, OrderCard
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'phone_number')


class WaiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'details', 'price')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'description')


class OrderCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'waiter', 'order', 'location')



admin.site.register(Client, ClientAdmin)
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(OrderCard, OrderCardAdmin)
