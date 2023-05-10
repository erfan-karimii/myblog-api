from rest_framework import serializers
from blog.models import Blog , Category
from django.utils.text import Truncator

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

class HyperBlogSerializer(serializers.HyperlinkedModelSerializer):
    # my_text = "Lorem ipsum dolor sit amet"
    # n_words = 3
    # truncated_text = Truncator(my_text).words(n_words)
    text = serializers.CharField()
    class Meta:
        model = Blog
        fields = ['url','title','author','text','create_date','image','status_publish',]
        extra_kwargs = {
            'author': {'lookup_field': 'pk'}
        }
    
    def get_text(self):
        print('','%'*100)

