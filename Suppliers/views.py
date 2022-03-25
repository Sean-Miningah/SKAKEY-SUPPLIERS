from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import permission_classes 
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response 
from rest_framework import viewsets 
from rest_framework import mixins 
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated 

from .models import (SupplierCompany, SupplierAccountRole, WareHouse, StockDetails, Products, ProductCategory)
from .serializers import (SupplierAccountSerializer, SupplierCompanySerializer, SupplierAccountRoleSerializer, 
                          WareHouseSerializer, StockDetailsSerializer, ProductSerializer, ProductCategorySerializer)

from .utilities import (get_and_authenticate_supplierAccount, generate_key)
from .send_mail import verification_email


SuppliersAccount = get_user_model()


class AccountAuthenticationView(mixins.CreateModelMixin, viewsets.GenericViewSet,):
    querset = SuppliersAccount.objects.all()
    serializer_class = SupplierAccountSerializer
    
    def create(self, request, *args, **kwargs):
        email = request.data['email']
        key = generate_key()
        verification_email(email,key)
        res = {
            'key': key
        }
        return Response(res, status=status.HTTP_200_OK)


class SupplierAccountView(mixins.CreateModelMixin,
                          viewsets.GenericViewSet,):
    
    queryset = SuppliersAccount.objects.all()
    serializer_class = SupplierAccountSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        account = SuppliersAccount.objects.get(email=request.data['email'])
        account.set_password(request.data['password'])
        account.save()
        token = Token.objects.create(user=account)
        
        res = {
            "message": "Succesfully registered Account",
            "token": "Token " + token.key
        }

        return Response(res, status=status.HTTP_201_CREATED, headers=headers)

class SupplierCompanyView(viewsets.ModelViewSet):
    queryset = SupplierCompany.objects.all()
    serializer_class = SupplierCompanySerializer
  
    
class SupplierRoleView(viewsets.ModelViewSet):
    queryset = SupplierAccountRole.objects.all()
    serializer_class = SupplierAccountRoleSerializer
    
class AccountLogin(viewsets.GenericViewSet,
                   mixins.CreateModelMixin):
    queryset = SuppliersAccount.objects.all()
    serializer_class = SupplierAccountSerializer 
    
    def create(self, request, *args, **kwargs):
        
        FAIL = '210'
        SUCCESS = '200'
        
        email = request.data["email"]
        password = request.data["password"]
        
        supplierAccount = get_and_authenticate_supplierAccount(email, password)
        token = Token.objects.get(user=supplierAccount)
        
        if supplierAccount.supplierCompany == None:
            code = FAIL
        else: 
            code = SUCCESS
        
        res = {
            "message": "Succesfully logged in to Account",
            "token": "Token " + token.key,
            "code":code 
        }
        
        return Response(res, status=status.HTTP_200_OK)
    
class WareHouserView(viewsets.ModelViewSet):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouserSerializer
    
class StockView(viewsets.ModelViewSet):
    queryset = StockDetails.objects.all()
    serializer_class = StockDetailsSerializer
    
class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
class ProductCategory(viewsets.ModelViewSet):
    queryset = ProductCategory.object.all()
    serializer_class = ProductCategorySerializer

