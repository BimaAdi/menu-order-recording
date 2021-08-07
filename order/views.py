from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from order.serializers import OrderSerializers
from order.models import Order

class OrderList(generics.GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def get(self, request, format=None):
        menus = Order.objects.all()
        serializer = OrderSerializers(instance=menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        input_data = OrderSerializers(data=request.data)
        input_data.is_valid(raise_exception=True)
        input_data.save()
        return Response(input_data.data, status=status.HTTP_201_CREATED)

class OrderDetail(generics.GenericAPIView):

    serializer_class = OrderSerializers

    def get(self, request, pk=None, format=None):
        menu = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializers(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        menu = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializers(instance=menu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, format=None):
        menu = get_object_or_404(Order, pk=pk)
        menu.delete()
        return Response('', status=status.HTTP_204_NO_CONTENT)
