import json
from typing import Union
from app.common.response import (
    Success, Created, SuccessNoContent,
    NotFound, 
    InternalServerError
)
from app.common.cache import get_cache, set_cache, delete_cache
from menu.serializers import MenuSerializers
from menu.models import Menu

def get_all_menu()->Union[Success, InternalServerError]:
    try:
        data = get_cache(key='menu_all')
        if data:
            return Success(data)
        else:
            menus = Menu.objects.all()
            serializer = MenuSerializers(instance=menus, many=True)

            set_cache(key='menu_all', value=serializer.data)
            return Success(serializer.data)
    except Exception as e:
        return InternalServerError(str(e))

def create_menu(serializer:MenuSerializers)->Union[Created, InternalServerError]:

    try:
        data = serializer.data
        new_menu = Menu.objects.create(**data)

        delete_cache(['menu_all'])
    except Exception as e:
        return InternalServerError(str(e))

    new_serializer = MenuSerializers(instance=new_menu)
    return Created(new_serializer.data)

def get_menu(id:int)->Union[Success, NotFound, InternalServerError]:
    try:
        data = get_cache(key=f'menu_{id}')
        if data:
            return Success(data)
        else:
            data = Menu.objects.get(pk=id)
            serializer = MenuSerializers(instance=data)

            set_cache(key=f'menu_{id}', value=serializer.data)
            return Success(serializer.data)
    except Menu.DoesNotExist:
        return NotFound()
    except Exception as e:
        return InternalServerError(str(e))

def update_menu(id:int, serializer:MenuSerializers)->Union[Success, NotFound, InternalServerError]:
    try:
        input_data = serializer.data
        data = Menu.objects.get(pk=id)
        data.name = input_data['name']
        data.price = input_data['price']
        data.save()

        serializer = MenuSerializers(instance=data)
        delete_cache([f'menu_{id}', 'menu_all'])
        return Success(serializer.data)
    except Menu.DoesNotExist:
        return NotFound()
    except Exception as e:
        return InternalServerError(str(e))

def patch_menu(id:int, input_data:dict)->Union[Success, NotFound, InternalServerError]:
    try:
        data = Menu.objects.get(pk=id)
        if 'name' in input_data.keys():
            data.name = input_data['name']
        if 'price' in input_data.keys():
            data.price = input_data['price']
        data.save()

        serializer = MenuSerializers(instance=data)
        delete_cache([f'menu_{id}', 'menu_all'])
        return Success(serializer.data)
    except Menu.DoesNotExist:
        return NotFound()
    except Exception as e:
        return InternalServerError(str(e))

def delete_menu(id:int)->Union[SuccessNoContent, NotFound, InternalServerError]:
    try:
        data = Menu.objects.get(pk=id)
        data.delete()

        delete_cache([f'menu_{id}', 'menu_all'])
        return SuccessNoContent()
    except Menu.DoesNotExist:
        return NotFound()
    except Exception as e:
        return InternalServerError(str(e))
    