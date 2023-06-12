from django.shortcuts import render
from djangonepal.models import Province,District,Municipality
from .serializer import ProvinceSerializer,MunicipalitySerializzer,DistrictSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from . import filters

class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    serializer_class = DistrictSerializer
    filterset_class = filters.DistrictFilter
    serializer_class = DistrictSerializer

class MunicipalityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Municipality.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = filters.MunicipalityFilter

    serializer_class = MunicipalitySerializzer


def html_view(request):
    data = Municipality.objects.all()

    return render(request,'djangonepalapp/index.html',{'response':data})