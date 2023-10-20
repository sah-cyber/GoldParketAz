import django_filters
from .models import *




class OrderFilter(django_filters.FilterSet):

    # name = django_filters.CharFilter(label='Mehsula gore')
    # categoriya = django_filters.CharFilter(label='Kategoriya uzre')
    # contry = django_filters.CharFilter(label='Olkeye gore')
    class Meta:
        model = Shop
        fields = ['name','categoriya']







