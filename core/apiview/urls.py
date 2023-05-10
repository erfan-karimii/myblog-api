from django.urls import path
from . import views

app_name='apiview'

urlpatterns = [
    path('authors/',views.author_info_api, name='authors-api-view'),
    path('home/',views.home_api, name='home-api-view'),

]
