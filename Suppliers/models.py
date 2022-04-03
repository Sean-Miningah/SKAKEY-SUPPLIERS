from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("An email must be provided")

        user = self.model(email=email, **other_fields)

        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, password, **other_fields)

class SuppliersAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=100)
    supplierCompany = models.ForeignKey('SupplierCompany', related_name='supplierCompany',
                                        on_delete=models.CASCADE, blank=True, 
                                        null=True, default=None)
    role = models.ForeignKey('SupplierAccountRole', related_name='supplierRole', 
                             on_delete=models.CASCADE, blank=True, null=True,
                             default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomAccountManager() 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
class SupplierCompany(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    businessIdentityNo = models.CharField(max_length=100, blank=False,
                                        null=False, unique=True)
    
    def __str__(self):
        return self.name
    
class SupplierAccountRole(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False, unique=True)
    
    def __str__(self):
        return self.name

class WareHouse(models.Model):
    supplierCompany = models.ForeignKey('SupplierCompany', on_delete=models.CASCADE, blank=False,
                                   null=False, default=None)
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    
    def __str__(self):
        return self.name

class StockDetails(models.Model):
    # stock quantity
    stockQuantity = models.BigIntegerField() 
    # price per unit
    pricePerUnit = models.BigIntegerField()
    wareHouse = models.ForeignKey('WareHouse', on_delete=models.CASCADE, blank=False,
                                    null=False, default=None)
    product = models.ForeignKey('Products', on_delete=models.CASCADE, blank=True,
                                 null=True, default=None)   
    out_of_stock = models.BooleanField(default=False)
    unitOfMeasure = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.product.name + ' ---- ' + self.wareHouse.name
    

class Products(models.Model):
    image = models.ImageField(upload_to='Products/image/', null=True, blank=True)
    name = models.CharField(max_length=100, blank=False, null=False, default=None)
    barcode = models.BigIntegerField()
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE,
                                 blank=True, null=True, default=None)
    unitOfMeasure = models.CharField(max_length=30, blank=True, null=True)
    altunitOfMeasure = models.CharField(max_length=30, blank=True, null=True)
    UOMConversion = models.BigIntegerField()
    
    def __str__(self):
        return self.name
    
# create a table to store the unit of measure
    
class ProductCategory(models.Model):
    # diary, sugar, cereals, flour
    name = models.CharField(max_length=100, unique=True, null=False)
    
    def __str__(self):
        return self.name