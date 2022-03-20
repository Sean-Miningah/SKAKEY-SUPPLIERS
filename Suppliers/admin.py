from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (SuppliersAccount, SupplierCompany, SupplierAccountRole)

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




admin.site.register(SuppliersAccount, SupplierAccountAdmin)
admin.site.register(SupplierCompany, SupplierCompanyAdmin)
admin.site.register(SupplierAccountRole,SupplierAccountRoleAdmin)