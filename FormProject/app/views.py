from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
# Create your views here.

def register(request):
    if request.method =='POST':
        Name=request.POST.get('name')
        Phone_No=request.POST.get('pno')
        Email=request.POST.get('email')
        Addres=request.POST.get('add')
        Gender=request.POST.get('gender')
        Course=request.POST.get('course')
        Username=request.POST.get('un')
        Password=request.POST.get('pw')
        
        RO=Register(Name=Name,Phone_No=Phone_No,Email=Email,Addres=Addres,Gender=Gender,Course=Course,Username=Username,Password=Password)
        RO.save()
        return HttpResponse("Done")
    return render(request,'register.html')

def form_register(request):
    EMRF=ModelRegisterForm()
    d={'EMRF':EMRF}
    if request.method == 'POST':
        Name=request.POST.get('Name')
        Phone_No=request.POST.get('Phone_No')
        Email=request.POST.get('Email')
        Addres=request.POST.get('Addres')
        Gender=request.POST.get('Gender')
        Course=request.POST.get('Course')
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        
        ERO=Register(Name=Name,Phone_No=Phone_No,Email=Email,Addres=Addres,Gender=Gender,Course=Course,Username=Username,Password=Password)
        ERO.save()
        return HttpResponse("Done")
        
    return render(request,'form_register.html',d)
        