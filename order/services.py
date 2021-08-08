from typing import Union
from django.db import transaction
from app.common.response import (
    Success, Created, SuccessNoContent,
    NotFound, 
    InternalServerError
)
from app.common.cache import get_cache, set_cache, delete_cache
from order.serializers import OrderSerializers
from order.models import Order, OrderMenu

def get_all_order()->Union[Success, InternalServerError]:
    try:
        data = get_cache(key='order_all')
        if data:
            return Success(data)
        else:
            data = Order.objects.all()
            serializer = OrderSerializers(instance=data, many=True)

            set_cache(key='order_all', value=serializer.data)
            return Success(serializer.data)
    except Exception as e:
        return InternalServerError(str(e))

def create_order(serializer:OrderSerializers)->Union[Created, InternalServerError]:

    try:
        data = serializer.data
        with transaction.atomic():
            new_order = Order.objects.create(
                table_number=data['table_number']
            )
            for item in data['order_menus']:
                OrderMenu.objects.create(order=new_order, **item)

        delete_cache(['order_*'])
    except Exception as e:
        return InternalServerError(str(e))

    new_serializer = OrderSerializers(instance=new_order)
    return Created(new_serializer.data)

def get_order(id:int)->Union[Success, NotFound, InternalServerError]:
    try:
        data = get_cache(key=f'order_{id}')
        if data:
            return Success(data)
        else:
            data = Order.objects.get(pk=id)
            serializer = OrderSerializers(instance=data)

            set_cache(key=f'order_{id}', value=serializer.data)
            return Success(serializer.data)
    except Order.DoesNotExist:
        return NotFound()
    except Exception as e:
        return InternalServerError(str(e))

def update_order(id:int, serializer:OrderSerializers)->Union[Success, NotFound, InternalServerError]:
    try:
        input_data = serializer.data
        with transaction.atomic():
            data = Order.objects.get(pk=id)
            data.table_number = input_data['table_number']
            data.save()
            
            data.order_menus.all().delete()
            for item in input_data['order_menus']:
                OrderMenu.objects.create(order=data, **item)

        serializer = OrderSerializers(instance=data)
        delete_cache([f'order_{id}', 'order_all'])
        return Success(serializer.data)
    except Order.DoesNotExist:
        return NotFound()
    except Exception as e:
        return InternalServerError(str(e))
    
def delete_order(id:int)->Union[SuccessNoContent, NotFound, InternalServerError]:
    try:
        data = Order.objects.get(pk=id)
        data.delete()

        delete_cache([f'order_{id}', 'order_all'])
        return SuccessNoContent()
    except Order.DoesNotExist:
        return NotFound()
    except Exception as e:
        return InternalServerError(str(e))
    