from django.contrib.auth.models import Group, User
from itec.models import (
    Asset,
    AccountablePropertyOfficer,
    PropertyCustodianAccount,
    UnitInformationCode,
    PropertyCustodian,
)
from rest_framework import serializers


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'id',
            'item_description',
            'manufacturer_name',
            'manufacturer_model_number',
            'serial_number',
            'building_number',
            'room_number',
            'cube_number',
            'ok',
            'classification',
            'comments',
        ]


class AccountablePropertyOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountablePropertyOfficer
        fields = '__all__'


class PropertyCustodianAccountSerializer(serializers.ModelSerializer):
    primary = serializers.StringRelatedField()
    alternate = serializers.StringRelatedField()
    assets = AssetBasicSerializer(many=True)

    class Meta:
        model = PropertyCustodianAccount
        fields = '__all__'


class UnitInformationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitInformationCode
        fields = '__all__'


class PropertyCustodianSerializer(serializers.ModelSerializer):
    property_custodian_account = serializers.StringRelatedField()
    uic = serializers.StringRelatedField()
    accountable_property_officer = serializers.StringRelatedField()

    class Meta:
        model = PropertyCustodian
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'first_name', 'last_name']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
