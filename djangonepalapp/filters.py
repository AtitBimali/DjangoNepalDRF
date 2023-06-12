import django_filters
from django.db.models import Q
from djangonepal.models import Municipality,District

class MunicipalityFilter(django_filters.FilterSet):
    province = django_filters.CharFilter(field_name='province__name',lookup_expr='icontains')
    district = django_filters.CharFilter(field_name='district__district',lookup_expr='icontains')

    class Meta:
        model = Municipality
        fields = ['province', 'district']

class DistrictFilter(django_filters.FilterSet):
    province = django_filters.CharFilter(field_name='province__name',lookup_expr='icontains')

    class Meta:
        model = District
        fields = ['province',]