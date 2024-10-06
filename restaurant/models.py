from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Waiter(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Order(models.Model):
    details = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return str(self.id)

class Location(models.Model):
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.address

class OrderCard(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
