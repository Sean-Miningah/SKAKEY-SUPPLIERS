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
                          WareHouseSerializer, StockDetailsSerializer, ProductsSerializer, ProductCategorySerializer,
                          WareHouseStockSerializer)
from .permissions import SubordinateUserCreation

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
    permission_classes = [IsAuthenticated]
    queryset = SupplierCompany.objects.all()
    serializer_class = SupplierCompanySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        account = SuppliersAccount.objects.get(id=self.request.user.id)
        company = SupplierCompany.objects.get(businessIdentityNo=request.data['businessIdentityNo'])
        account.supplierCompany = company
        account.save()
        
        res = {
            "message": "Succesfully registered Account",
        }

        return Response(res, status=status.HTTP_201_CREATED, headers=headers)
    
class CompanyView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierCompanySerializer
    
    def get_queryset(self):
        queryset = SupplierCompany.objects.all()
        user = self.request.user 
        account = SuppliersAccount.objects.get(email=user)
        company = queryset.filter(id=account.supplierCompany.id)
        return company
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data.pop(0)
        return Response(data)
    
    
class SupplierRoleView(viewsets.ModelViewSet):
    queryset = SupplierAccountRole.objects.all()
    serializer_class = SupplierAccountRoleSerializer
    
class SubordinateAccountView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, SubordinateUserCreation]
    queryset = SuppliersAccount.objects.all()
    serializer_class = SupplierAccountSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # creator = SuppliersAccount.objects.get(id=self.request.user)
        creator = self.request.user
        creatorCompany = creator.supplierCompany.id
        
        account = SuppliersAccount.objects.get(email=request.data['email'])
        company = SupplierCompany.objects.get(id=creatorCompany)
        account.set_password(request.data['password'])
        account.supplierCompany = company
        account.save()
        token = Token.objects.create(user=account)
        
        res = {
            "message": "Succesfully registered Account",
        }

        return Response(res, status=status.HTTP_201_CREATED, headers=headers)
        
    
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
    
class WareHouseView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer
    
    def list(self, request, *args, **kwargs):
        account = self.request.user
        company = SupplierCompany.objects.get(id=account.supplierCompany.id)
        warehouse = WareHouse.objects.filter(supplierCompany=company.id)
        print(warehouse)
        serializer = WareHouseSerializer(warehouse, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
class StockView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = StockDetails.objects.all()
    serializer_class = StockDetailsSerializer
    
    # Api gets a list of products to add to it's stockDetails
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        warehouse = WareHouse.objects.get(id=serializer.data.pop(0)["wareHouse"])
        
        message = "Succesfully Added Stock to WareHouse " + warehouse.name
        
        res = {
            "message": message
        }
        
        return Response(res,status=status.HTTP_200_OK)
    
    def list(self, request,*args,**kwargs):
        print(request.headers)
        wareHouse = WareHouse.objects.get(id=request.headers['warehouse'])
        warehouseStocks = StockDetails.objects.filter(wareHouse=wareHouse)
        serializer = WareHouseStockSerializer(warehouseStocks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ProductView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
    
    
class ProductCategory(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

