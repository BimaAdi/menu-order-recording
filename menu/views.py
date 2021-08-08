from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from menu.serializers import MenuSerializers
from menu.models import Menu
from menu.services import (
    get_all_menu, 
    create_menu,
    get_menu,
    update_menu,
    delete_menu
)
from app.common.response import common_response

class MenuHighlight(generics.GenericAPIView):

    queryset = Menu.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        menu = self.get_object()
        return Response(menu.highlighted)

class MenuList(generics.GenericAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

    def get(self, request, format=None):
        output_data = get_all_menu()
        return common_response(output_data)

    def post(self, request, format=None):
        input_data = MenuSerializers(data=request.data)
        input_data.is_valid(raise_exception=True)
        output_data = create_menu(input_data)
        return common_response(output_data)

class MenuDetail(generics.GenericAPIView):

    serializer_class = MenuSerializers

    def get(self, request, pk=None, format=None):
        output_data = get_menu(id=pk)
        return common_response(output_data)

    def put(self, request, pk=None, format=None):
        serializer = MenuSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        output_data = update_menu(id=pk, serializer=serializer)
        return common_response(output_data)

    def delete(self, request, pk=None, format=None):
        output_data = delete_menu(id=pk)
        return common_response(output_data)
