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

    def create(self, validated_data):
        order_menus = validated_data.pop('order_menus')
        order = Order.objects.create(**validated_data)
        for item in order_menus:
            OrderMenu.objects.create(order=order, **item)
        return order

    def update(self, instance, validated_data):
        order_menus = validated_data.pop('order_menus')
        instance.table_number = validated_data.get('table_number', instance.table_number)
        instance.order_menus.all().delete()
        for item in order_menus:
            OrderMenu.objects.create(order=instance, **item)
        return instance
    