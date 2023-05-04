from os import stat
from django.http import HttpResponse
from django.shortcuts import render
from .models import contactModel
from .forms import contactForm
# Create your views here.



def contactus(request):
    
    if request.method == "POST" :
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            massage = form.cleaned_data['massage']
            form = contactModel.objects.create(name=name,subject=subject,massage=massage)
            form.save()
        return HttpResponse("saved!")
    else:
        form = contactForm()
    return render(request,'account_folder/contact.html',{'form':form,'navbar':'contactus'})
        