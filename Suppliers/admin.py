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
    list_filter = ('name',)
    
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
    list_display = ('id', 'name', 'supplierCompany',)
    search_fields = ('id', 'name', 'supplierCompany',)
    
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
    list_display = ('id', 'pricePerUnit', 'wareHouse', 'product')
    search_fields = ('id', 'product',)
    
    fieldsets = (
        (None, {'fields':('pricePerUnit', 'wareHouse', 'product', 'stockQuantity')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('pricePerUnit', 'wareHouse', 'stockQuantity', 'product')
        })
    )


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('id', 'name', 'category')
    
    fieldsets = (
        (None, {'fields':('name', 'category', 'barcode')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('name', 'barcode', 'category', 'barcode')
        })
    )

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    
    fieldsets = (
        (None, {'fields':('name',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('name',)
        })
    )
    
    
admin.site.register(StockDetails, StockDetailsAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(WareHouse, WareHouseAdmin)
admin.site.register(SuppliersAccount, SupplierAccountAdmin)
admin.site.register(SupplierCompany, SupplierCompanyAdmin)
admin.site.register(SupplierAccountRole,SupplierAccountRoleAdmin)