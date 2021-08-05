import django_filters

from shop.models import Order, OrderItem

class OrderFilterCode(django_filters.FilterSet):
    
     class Meta:
         model = Order
         fields = ['order_code', 'status']



        