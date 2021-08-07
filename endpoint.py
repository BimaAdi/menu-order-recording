from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'menu': reverse('menu-list', request=request, format=format),
        'menu_detail': reverse('menu-detail', args=['1'], request=request, format=format)
    })
