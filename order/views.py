from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from order.serializers import OrderSerializers
from order.models import Order
from order.services import ( 
    get_all_order,
    create_order,
    get_order,
    update_order,
    delete_order
)
from app.common.response import common_response

class OrderList(generics.GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def get(self, request, format=None):
        data = get_all_order()
        return common_response(data)

    def post(self, request, format=None):
        serializer = OrderSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        output_data = create_order(serializer=serializer)
        return common_response(output_data)

class OrderDetail(generics.GenericAPIView):

    serializer_class = OrderSerializers

    def get(self, request, pk=None, format=None):
        output_data = get_order(id=pk)
        return common_response(output_data)

    def put(self, request, pk=None, format=None):
        serializer = OrderSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        output_data = update_order(id=pk, serializer=serializer)
        return common_response(output_data)

    def delete(self, request, pk=None, format=None):
        output_data = delete_order(id=pk)
        return common_response(output_data)
