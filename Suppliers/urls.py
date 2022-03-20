from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from . import views 

router = DefaultRouter()
router.register("supplierAccount", views.SupplierAccountView, basename="create-account")
router.register("supplierCompany", views.SupplierCompanyView, basename="create-company")
router.register("accountRoles", views.SupplierRoleView, basename="supplier-role")
router.register("login", views.AccountLogin, basename="login")

urlpatterns = [
    path('suppliers/', include(router.urls)),
]