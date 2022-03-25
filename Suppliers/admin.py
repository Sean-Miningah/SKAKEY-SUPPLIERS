from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (SuppliersAccount, SupplierCompany, SupplierAccountRole,
                    WareHouse, StockDetails, Products, ProductCategory)

# Register your models here.

class SupplierAccountAdmin(UserAdmin):
    ordering = ('-start_date',)
    search_fields = ('role', 'start_date', 'supplierCompany', 'email')
    list_display = ('id', 'email', 'supplierCompany', 'role')
    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields':('email', 'password', 'supplierCompany', 'role',)}),
        ('Permissions', {'fields':('is_staff', 'is_active',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('email', 'supplierCompany', 'role', 'password1', 
                      'password2', 'is_staff', 'is_active')
        }),
    )
    
class SupplierCompanyAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name', 'businessIdentityNo')
    list_display = ('id', 'name', 'businessIdentityNo')
    
    fieldsets = (
        (None, {'fields':('name', 'businessIdentityNo')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('name', 'businessIdentityNo')
        })
    )

class SupplierAccountRoleAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
    list_display = ('id', 'name')
    
    fieldsets = (
        (None, {'fields':('name',)}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('name',)
        })
    )

class WareHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplierCompany',)
    search_fields = ('name', 'supplierCompany',)
    
    fieldsets = (
        (None, {'fields':('name', 'longitude', 'latitude', 'supplierCompany')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('name','longitude', 'latitude', 'supplierCompany')
        })
    )

class StockDetailsAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class ProductCategoryAdmin(admin.ModelAdmin):
    pass



admin.site.register(WareHouse, WareHouseAdmin)
admin.site.register(SuppliersAccount, SupplierAccountAdmin)
admin.site.register(SupplierCompany, SupplierCompanyAdmin)
admin.site.register(SupplierAccountRole,SupplierAccountRoleAdmin)