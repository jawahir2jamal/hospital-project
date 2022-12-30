from django.shortcuts import render

from .models import Departments, Doctors
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")  
def booking(request):
    if request.method=="POST":
        form1=BookingForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,"conformation.html")
    formvalue=BookingForm()
    dict_form={
        'formkey':formvalue
    }
    return render(request,"booking.html",dict_form)   
def doctors(request):
    dict_doct={
        'doc':Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doct)           
def contact(request):
    return render(request,"contact.html")   
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    } 
    return render(request,"department.html",dict_dept)   

def logi(request):
    return render(request,"login.html")      
            

