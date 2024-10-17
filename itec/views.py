from django.contrib.auth.models import Group, User
from django.http import HttpResponse

from rest_framework.decorators import action
from rest_framework import permissions, viewsets

from itec.serializers import GroupSerializer, UserSerializer
from itec.excel import exportToExcel


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom action to export user data
    @action(detail=False, methods=['get'], url_path='export-users')
    def export_users(self, request):
        userList = User.objects.all().values()
        exportToExcel(list(userList), UserSerializer)
        return HttpResponse(status=204)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
