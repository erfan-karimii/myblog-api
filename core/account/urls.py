from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('login/',views.loginview,name='login'),
    path('register/',views.SignUpview,name='register'),
	path('logout/',views.LogOut,name='logout'),
	path('deactive/',views.deactive_profile,name='deactive'),
	path('profile/',views.list_author_blog,name='profile'),
	path('update_user/<pk>',views.UpdateDetailUser.as_view(),name='update_user'),
	path('create_blog/',views.CreateBlogPost.as_view(),name='create_blog'),
	path('update_blog/<pk>',views.UpdateBlogPost.as_view(),name='update_blog'),
	path('delete_blog/<pk>',views.DeleteBlogPost.as_view(),name='delete_blog'),

     
]
