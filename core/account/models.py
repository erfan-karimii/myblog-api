from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class AccountDetail(models.Model):
    user_account=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True,unique=True)
    last_name = models.CharField(max_length=100,null=True,unique=True)
    email = models.EmailField(max_length=100,null=True)
    phone_number = models.IntegerField(null=True)
    state = models.CharField(max_length=50,null=True)
    avatar = models.ImageField(null=True)
    def __str__(self):
        return str(self.user_account)
    def get_absolute_url(self):
        return reverse("account:profile")
    