from django.contrib.auth.models import User, Group 
from rest_framework import viewsets ,generics
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer , AccountInfoSerializer
from account.models import AccountInfo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountInfoListVIew(generics.ListAPIView):
    queryset = AccountInfo.objects.all()
    serializer_class = AccountInfoSerializer