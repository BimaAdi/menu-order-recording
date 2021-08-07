from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from menu.views import MenuViews
from menu.views import MenuList, MenuDetail, MenuHighlight

urlpatterns = format_suffix_patterns([
    path('', MenuList.as_view(), name='menu-list'),
    path('<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
    path('<int:pk>/highlight/', MenuHighlight.as_view(), name='menu-higlight')
])
