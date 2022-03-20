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
    
