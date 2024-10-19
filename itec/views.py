from django.contrib.auth.models import Group, User
from itec.models import Asset
from django.http import HttpResponse

from rest_framework.decorators import action
from rest_framework import permissions, viewsets

from itec.serializers import AssetSerializer, AssetBasicSerializer, GroupSerializer, UserSerializer
from itec.excel import exportToExcel

from rest_framework.response import Response

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('item_description')
    serializer_class = AssetSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path='basic')
    def basic(self, request, *args, **kwargs):
        assets = self.get_queryset()
        serializer = AssetBasicSerializer(assets, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='export-users')
    def export_users(self, request):
        userList = User.objects.all().values()
        exportToExcel(list(userList), UserSerializer)
        return HttpResponse(status=204)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
