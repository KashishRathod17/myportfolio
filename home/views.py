from django.shortcuts import render,HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import *
    
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def skills(request):
    skills = Skills.objects.all() 
    return render(request,'skills.html',{'skills':skills})

def projects(request):
    project = Project.objects.all()
    return render(request,'projects.html',{'project':project})

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        msg=request.POST['msg']
        contact = Contact(name=name,email=email,phone=phone,msg=msg,date=datetime.today())
        contact.save()
        print("data written")
    return render(request,'contact.html')
    