from django.contrib.auth.models import Group, User
from itec.models import Asset
from rest_framework import serializers


class FullAssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = []


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
