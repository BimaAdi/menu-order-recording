from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from menu.serializers import MenuSerializers
from menu.models import Menu

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
        menus = Menu.objects.all()
        serializer = MenuSerializers(instance=menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        input_data = MenuSerializers(data=request.data)
        input_data.is_valid(raise_exception=True)
        input_data.save()
        return Response(input_data.data, status=status.HTTP_201_CREATED)

class MenuDetail(generics.GenericAPIView):

    serializer_class = MenuSerializers

    def get(self, request, pk=None, format=None):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializers(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializers(instance=menu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, format=None):
        menu = get_object_or_404(Menu, pk=pk)
        menu.delete()
        return Response('', status=status.HTTP_204_NO_CONTENT)
