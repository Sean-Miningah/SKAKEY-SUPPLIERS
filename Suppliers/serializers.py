from django.contrib.auth import get_user_model 
from rest_framework import serializers

from .models import (SupplierCompany, SupplierAccountRole, WareHouse,
                     StockDetails, Products, ProductCategory)
SuppliersAccount = get_user_model() 

class SupplierAccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SuppliersAccount 
        exclude = ['is_staff','is_active','password']
        
        def create(self, validated_data):
            password = validated_data.pop('password')
            account = SuppliersAccount(**validated_data)
            print('\n  acount run \n')
            account.save()
            return account
        
class SupplierCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierCompany 
        fields = '__all__'    
        
class SupplierAccountRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierAccountRole
        fields = '__all__'   
        
class WareHouseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = WareHouse
        fields = '__all__'
        
class StockDetailsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StockDetails
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Products
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductCategory
        fields = '__all__'