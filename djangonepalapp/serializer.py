from rest_framework import serializers
from djangonepal.models import Province,Municipality,District

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Province
        fields=['name']

class DistrictSerializer(serializers.ModelSerializer):
    province = serializers.CharField(source='province.name')
    class Meta:
        model= District
        fields=['province','district']

class MunicipalitySerializzer(serializers.ModelSerializer):
    province = serializers.CharField(source='province.name')
    district = serializers.CharField(source='district.district')

    class Meta:
        model = Municipality
        fields = ['province','district','municipality']
