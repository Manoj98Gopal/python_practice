from django.shortcuts import render
from django.http import HttpResponse
from store.models import Customer

# Create your views here.
def say_hello(request):
    
    customers = Customer.objects.all()
    
    return render(request,'hello.html',{'customers': customers})