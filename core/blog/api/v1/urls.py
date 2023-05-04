from django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path('', views.api_root),
    path('blogs/', views.BlogList.as_view(),name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetail.as_view(),name='blog-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)