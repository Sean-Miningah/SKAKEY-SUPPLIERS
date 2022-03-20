from django.contrib.auth import get_user_model 
from rest_framework import serializers

from .models import (SupplierCompany, SupplierAccountRole)
SuppliersAccount = get_user_model() 

class SupplierAccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SuppliersAccount 
        fields = ('email', 'password', 'supplierCompany', 'role')
        
class SupplierCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierCompany 
        fields = '__all__'    
        
class SupplierAccountRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierAccountRole
        fields = '__all__'   