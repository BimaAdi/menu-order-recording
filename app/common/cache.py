import json
from typing import Union
from django.core.cache import cache

def get_cache(key:str)->Union[dict, None]:
    data = cache.get(key)
    if data:
        return json.loads(data)
    return None

def set_cache(key:str, value:dict):
    cache.set(key, str(json.dumps(value)))

def delete_cache(patterns:list):
    '''
    patterns: list of str
    '''
    for item in patterns:
        cache.delete_pattern(item)
