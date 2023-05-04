from django.shortcuts import render , redirect
from .models import Blog, Category,Comment
from django.core.paginator import Paginator
from .forms import SearchForm,CommentForm
from account.models import AccountDetail

def home(request):
    last_posts = Blog.objects.filter(status_publish='publish').order_by('-create_date')[0:3]
    context = {
        'last_posts' : last_posts,
        'navbar':'home',
    }
    return render(request,'blog_folder/index.html',context)

def blogs(request):
    if request.GET and not request.GET.get('page'):
        form = SearchForm(request.GET)
        if form.is_valid():
            title = form.cleaned_data['title']

            page_obj = Blog.objects.filter(status_publish='publish',title__contains = title)
            categorys = Category.objects.all()
        else:
            form = SearchForm()
    else:
        blogs = Blog.objects.filter(status_publish='publish').order_by('-create_date')
        categorys = Category.objects.all()
        paginator = Paginator(blogs, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'navbar' : 'blogs',
        'page_obj' : page_obj,
        "categorys" : categorys,
        'navbar' : "blog",
        'form': SearchForm(request.GET),
    }
    return render(request,'blog_folder/blog.html',context)

def about_us(request) :
    context = {
        'navbar' : 'about-us',
    }
    return render(request,'blog_folder/about-us.html',context)

def authors_info(request):
    authors = AccountDetail.objects.all()
    context = {
        'navbar' : 'authors',
        'authors' : authors
    }
    return render(request,'blog_folder/team.html',context)

def detail_blog_view(request,id):
    blog = Blog.objects.get(id=id)
    detail_cat = Category.objects.filter(blog__id = id)
    comments = Comment.objects.filter(is_active=True,blog_id = id)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Full_name = comment_form.cleaned_data['Full_name']
            Email_address = comment_form.cleaned_data['Email_address']
            massage = comment_form.cleaned_data['massage']
            new_comment = Comment.objects.create(
                Full_name=Full_name,Email_address=Email_address,massage=massage,blog=blog
                )
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
    'blog':blog,
    'detail_cat':detail_cat,
    'comments':comments,
    "comment_form":comment_form,
    }
    return render(request,'blog_folder/blog-details.html',context)

def author_blog_view(request,auth_id):
    author_blogs = Blog.objects.filter(status_publish='publish',author_id=auth_id)
    return render(request, 'blog_folder/blog.html',{'page_obj':author_blogs})

def category_blog_view(request,cat):
    categorys = Category.objects.all()
    blog = Blog.objects.filter(status_publish='publish',category__name = cat)
    return render(request,'blog_folder/blog.html',{'page_obj':blog,"categorys" : categorys})
