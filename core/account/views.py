from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView , CreateView , DeleteView
from django.urls import reverse_lazy
from blog.models import Blog  
from .models import AccountDetail
# Create your views here.

def SignUpview(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
        else:
            error_view = "Pleas Try Again"
            return render(request,'account_folder/signup.html',{'form':form,'error_view':error_view})

    else:
        form = UserCreationForm()
        return render(request,'account_folder/signup.html',{'form':form,})


def loginview(request):         #context ino dorost konam

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            try:
                AccountDetail.objects.get(user_account_id=user.id)              
                return redirect('blog:home')
            except:
                AccountDetail.objects.create(user_account=user) 
                return redirect('blog:home')
            

        else:
            error_view = "Pleas Try Again"
            return render(request,'account_folder/login.html',{'form':form,'error_view':error_view})
    else:
        form = AuthenticationForm()
    
    return render(request,'account_folder/login.html',{'form':form})


def LogOut(request):
    logout(request)
    return redirect('blog:home')

def list_author_blog(request):
    blogs = Blog.objects.filter(status_publish='publish',author_id=request.user.id)
    account_de = AccountDetail.objects.get(user_account_id=request.user.id)
    return render(request,'account_folder/dashbord.html',{'author_blogs':blogs,'account_de':account_de})

class UpdateDetailUser(UpdateView):
    model = AccountDetail
    template_name = "account_folder/account_settings.html"
    fields= ['first_name','last_name','email','phone_number','state','avatar']
    
class UpdateBlogPost(UpdateView):
    model= Blog
    template_name = "account_folder/update_post.html"
    fields= ['title','text','category','image','status_publish']

class CreateBlogPost(CreateView):
    model= Blog
    template_name = "account_folder/create_post.html"
    fields= ['title','author','text','category','image']

class DeleteBlogPost(DeleteView):
    model = Blog
    template_name = 'account_folder/delete_post.html'
    success_url = reverse_lazy('account:profile')
def deactive_profile(request):        
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    messages.success(request, 'Profile successfully disabled.')
    return redirect('blog:home')