from django.contrib.auth.models import Group, User
from itec.models import Asset
from rest_framework import serializers


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'item_description', 'manufacturer_name', 'manufacturer_model_number', 'serial_number', 'sub_location', 'room_number', 'cube_number', 'ok', 'classification', 'comments']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
