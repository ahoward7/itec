from django.contrib.auth.models import Group, User
from itec.models import (
    AccountablePropertyOfficer,
    PropertyCustodianAccount,
    UnitInformationCode,
    PropertyCustodian,
    Asset,
)
from django.http import HttpResponse

from rest_framework.decorators import action
from rest_framework import permissions, viewsets

from itec import serializers
from itec.excel import exportToExcel

from rest_framework.response import Response


class AccountablePropertyOfficerViewSet(viewsets.ModelViewSet):
    queryset = AccountablePropertyOfficer.objects.all().order_by('name')
    serializer_class = serializers.AccountablePropertyOfficerSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropertyCustodianAccountViewSet(viewsets.ModelViewSet):
    queryset = PropertyCustodianAccount.objects.all().order_by('account_number')
    serializer_class = serializers.PropertyCustodianAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class UnitInformationCodeViewSet(viewsets.ModelViewSet):
    queryset = UnitInformationCode.objects.all().order_by('code')
    serializer_class = serializers.UnitInformationCodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropertyCustodianViewSet(viewsets.ModelViewSet):
    queryset = PropertyCustodian.objects.all().order_by('name')
    serializer_class = serializers.PropertyCustodianSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('item_description')
    serializer_class = serializers.AssetSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path='basic')
    def basic(self, request, *args, **kwargs):
        assets = self.get_queryset()
        serializer = serializers.AssetBasicSerializer(assets, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='export-users')
    def export_users(self, request):
        userList = User.objects.all().values()
        exportToExcel(list(userList), serializers.UserSerializer)
        return HttpResponse(status=204)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
