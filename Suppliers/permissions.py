from rest_framework import permissions
from .models import SupplierAccountRole as Role

class SubordinateUserCreation(permissions.BasePermission):
    
    TIER_ONE = "Tier 1"
    # TIER_TWO =  Role.objects.get(name="Tier 2").name
    # TIER_THREE = Role.objects.get(name="Tier 3").name
    # TIER_FOUR = Role.objects.get(name="Tier 4").name
    
    message = "Subordinate users cannot perform this action."
    
    def has_permission(self, request, view):
        accountRole = request.user.role.name 
        
        return accountRole == self.TIER_ONE
    
#     def has_object_permission(self, request, view, obj):
# #         pass