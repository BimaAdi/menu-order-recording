from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order.views import OrderList, OrderDetail

urlpatterns = format_suffix_patterns([
    path('', OrderList.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetail.as_view(), name='order-detail')
])
