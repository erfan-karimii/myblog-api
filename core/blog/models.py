from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    PUBLISH_CHOICE=(
        ('draft','draft'),
        ('publish','publish'),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(unique=True)
    create_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('Category')
    image = models.ImageField(null = True)
    status_publish=models.CharField(max_length=7,choices=PUBLISH_CHOICE,default='draft')


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("account:profile")
    

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    Full_name = models.CharField(max_length=200)
    Email_address = models.EmailField(max_length=254)
    massage = models.TextField(null=True,unique_for_date=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)