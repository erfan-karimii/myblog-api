from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status ,generics , viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from blog.models import Blog , Category
from .serializers import BlogSerializer , HyperBlogSerializer 
from django_filters import rest_framework as filters

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'blogs': reverse('blog-list', request=request, format=format),
        'account-infos': reverse('account-info-list', request=request, format=format),


    })
# class BlogList(APIView):
#     """
#     List all blogs, or create a new blog.
#     """
#     def get(self, request, format=None):
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = HyperBlogSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title','author','text','create_date','category',)


# class BlogDetail(APIView):
#     """
#     Retrieve, update or delete a blog instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesNotExist:
#             raise Http404
        
#     def get(self, request,pk, format=None):
#         blog = Blog.objects.get(id=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
    
#     def put(self, request,pk, format=None):
#         blog = self.get_object(id=pk)
#         serializer = BlogSerializer(blog,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = HyperBlogSerializer

