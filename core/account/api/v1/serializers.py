from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    test3 = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups','test3']
        extra_kwargs = {
            'url': {'view_name': 'blog-detail', 'lookup_field': 'id'},
        }
    
    def get_test3(self,obj):
        return 'test'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        