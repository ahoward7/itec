from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from itec import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'accountable-property-officers', views.AccountablePropertyOfficerViewSet)
router.register(r'property-custodian-accounts', views.PropertyCustodianAccountViewSet)
router.register(r'unit-information-codes', views.UnitInformationCodeViewSet)
router.register(r'property-custodians', views.PropertyCustodianViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
