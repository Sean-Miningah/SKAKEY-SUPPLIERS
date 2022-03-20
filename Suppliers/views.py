from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import permission_classes 
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response 
from rest_framework import viewsets 
from rest_framework import mixins 
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated 

from .models import (SupplierCompany, SupplierAccountRole)
from .serializers import (SupplierAccountSerializer, SupplierCompanySerializer, SupplierAccountRoleSerializer)


SuppliersAccount = get_user_model()


class SupplierAccountView(mixins.CreateModelMixin,
                          viewsets.GenericViewSet,):
    
    queryset = SuppliersAccount.objects.all()
    serializer_class = SupplierAccountSerializer


class SupplierCompanyView(viewsets.ModelViewSet):
    queryset = SupplierCompany.objects.all()
    serializer_class = SupplierCompanySerializer
  
    
class SupplierRoleView(viewsets.ModelViewSet):
    queryset = SupplierAccountRole.objects.all()
    serializer_class = SupplierAccountRoleSerializer