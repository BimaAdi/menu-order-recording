from rest_framework import serializers
from order.models import Order, OrderMenu

class OrderMenuSerializers(serializers.ModelSerializer):

    class Meta:
        model = OrderMenu
        fields = ['id', 'menu_name', 'price', 'qty']


class OrderSerializers(serializers.ModelSerializer):

    order_menus = OrderMenuSerializers(many=True)

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'order_date', 'order_menus']
    