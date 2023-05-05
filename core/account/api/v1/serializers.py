from django.contrib.auth.models import User, Group
from rest_framework import serializers
from account.models import AccountInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AccountInfoSerializer(serializers.ModelSerializer):
    autor_blog_relative_url = serializers.SerializerMethodField()
    class Meta:
        model = AccountInfo
        fields = ['user_account','first_name','last_name','email','phone_number','state','avatar','autor_blog_relative_url']
    
    def get_autor_blog_relative_url(self,obj):
        return f'/blog_author_view/{obj.user_account.id}'
