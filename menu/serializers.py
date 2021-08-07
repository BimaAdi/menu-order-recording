from rest_framework import serializers
from menu.models import Menu

class MenuSerializers(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'name', 'price']

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
        