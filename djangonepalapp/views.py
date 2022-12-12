from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from djangonepal.models import Province,District,Municipality
from .serializer import ProvinceSerializer,MunicipalitySerializzer,DistrictSerializer
import requests
# Create your views here.

@api_view(['GET'])
def getAll(request):
    # # province = Province.objects.all()
    # # district = District.objects.all()
    # municipality = Municipality.objects.all()
    # # provinceserializer = ProvinceSerializer(province, many=True)
    # # districtserializer = DistrictSerializer(district, many=True)
    # municipalityserializer = MunicipalitySerializzer(municipality, many=True)
    api_urls={
        'All':'/',
        'Provinces':'/province/',
        'District':'/district/',
        'Municipalities':'/municipality/',
        'Html View':'/html-veiw'

    }
    return Response(api_urls)


@api_view(['GET'])
def getProvince(request):
    province = Province.objects.all()
    provinceserializer = ProvinceSerializer(province, many=True)
    return Response(provinceserializer.data)

@api_view(['GET'])
def getDistrict(request):
    district = District.objects.all()
    districtserializer = DistrictSerializer(district, many=True)
    return Response(districtserializer.data)
    
@api_view(['GET'])
def getMunicipality(request):
    municipality = Municipality.objects.all()
    municipalityserializer = MunicipalitySerializzer(municipality, many=True)
    return Response(municipalityserializer.data)

def html_view(request):
    url='http://127.0.0.1:8000/municipality/'
    response = requests.get(url).json()

    return render(request,'djangonepalapp/index.html',{'response':response})