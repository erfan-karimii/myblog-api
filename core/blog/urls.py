from django.urls import path
from . import views


app_name = 'blog'



urlpatterns = [
    path('',views.home, name='home'),
    path('blogs/',views.blogs, name='blogs'),
    path('about-us/',views.about_us, name='about-us'),
    path('authors/',views.authors_info, name='authors'),
    path('blog_detail/<id>',views.detail_blog_view, name='detail'),
    path('blog/<cat>',views.category_blog_view, name='cat'),
    path('blog_author_view/<auth_id>',views.author_blog_view, name='auth'),
    
]