from rest_framework import serializers
from menu.models import Menu

class MenuSerializers(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'name', 'price']
        