from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from . import views 

router = DefaultRouter()
router.register("emailVerification", views.AccountAuthenticationView, basename="email-verification")
router.register("supplierAccount", views.SupplierAccountView, basename="create-account")
router.register("subordinateAccount", views.SubordinateAccountView, basename="subordinates-info")
router.register("supplierCompany", views.SupplierCompanyView, basename="create-company")
router.register("accountRoles", views.SupplierRoleView, basename="supplier-role")
router.register("login", views.AccountLogin, basename="login")

router.register("wareHouse", views.WareHouseView, basename="warehouse")
router.register("selfCompany", views.CompanyView, basename='selfwarehouse')
router.register("wareHouseStocks", views.StockView, basename="stocks")
router.register("products", views.ProductView, basename="products")
router.register("productCategories", views.ProductCategory, basename="productcategories")

urlpatterns = [
    path('suppliers/', include(router.urls)),
]