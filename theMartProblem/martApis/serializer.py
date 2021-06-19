from rest_framework import serializers
from martApis.models import Mart,Sku

class MartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mart
        fields = '__all__'    

class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = '__all__'            
        