from django.shortcuts import render

# Create your views here.

def author_info_api(request):
    return render(request,'api_blog_folder/team.html')


def home_api(request):
    # last_posts = Blog.objects.filter(status_publish='publish').order_by('-create_date')[0:3]
    # context = {
    #     'last_posts' : last_posts,
    #     'navbar':'home',
    # }
    return render(request,'api_blog_folder/index.html')