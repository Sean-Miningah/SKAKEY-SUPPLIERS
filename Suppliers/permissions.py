# from rest_framework import permissions
# from .models import SupplierAccountRole as Role

# class SubordinateUserCreationPermission(permissions.BasePermission):
    
#     TIER_ONE = Role.objects.get(name="Tier_1")
#     TIER_TWO =  Role.objects.get(name="Tier_2")
#     TIER_THREE = Role.objects.get(name="Tier_3")
#     TIER_FOUR = Role.objects.get(name="Tier_4")
    
#     message = "You are not allowed"
    
#     def has_permission(self, request, view):
#         pass
    
#     def has_object_permission(self, request, view, obj):
#         pass