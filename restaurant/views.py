from django.shortcuts import render

from restaurant.models import Client, Waiter, Order, Location, OrderCard


# Create your views here.
def index(request):
    clients = Client.objects.all()
    if request.GET.get('price'):
        result_set = OrderCard.objects.filter(order__price__gte=request.GET.get('price'))
        if not result_set:
            return render(request, 'restaurant/index.html', {'isHome': True, 'isEmpty': True,
                                                                                    'clients': clients})
        return render(request, 'restaurant/index.html', {'isHome':True, 'result_set':result_set,
                                                                            'clients': clients})
    elif request.GET.get('client'):
        result_set1 = OrderCard.objects.filter(client__id=request.GET.get('client'))
        return render(request, 'restaurant/index.html', {'isHome': True, 'result_set1': result_set1,
                                                         'clients': clients})
    return render(request, 'restaurant/index.html', {'isHome':True, 'clients': clients})


def clients(request):
    clients = Client.objects.all()
    return render(request, 'restaurant/index.html', {'isClients':True,
                                                                                'clients':clients})


def waiters(request):
    waiters = Waiter.objects.all()
    return render(request, 'restaurant/index.html', {'isWaiters':True,
                                                                            'waiters':waiters})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/index.html', {'isOrders':True,
                                                                            'orders':orders})


def locations(request):
    locations = Location.objects.all()
    return render(request, 'restaurant/index.html', {'isLocation':True,
                                                                            'locations':locations})


def order_card(request):
    order_cards = OrderCard.objects.all()
    return render(request, 'restaurant/index.html', {'isOrderCard':True,
                                                                            'ordercards':order_cards})
