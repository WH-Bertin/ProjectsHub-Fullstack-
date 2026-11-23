from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 
from .models import F_projects

# Create your views here.

def  index (request):
    projects = F_projects.objects.all().values()
    template = loader.get_template('index/index.html')
    context = {
        'projects': projects ,
    }
    return HttpResponse(template.render(context,request))

def login(request):
    return render(request,'login/login.html')
