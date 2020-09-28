from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    surveys = Survey.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_surveys = surveys.count()

    context = {'surveys':surveys,'customers':customers,'total_customers':total_customers,\
               'total_surveys':total_surveys}
    return render(request,'accounts/dashboard.html',context)

def customer(request,pk):
    customer = Customer.objects.get(id=pk)

    surveys = customer.survey_set.all()

    survey_count = surveys.count()
    
    context = {'customer':customer,'surveys':surveys,'survey_count':survey_count}
    return render(request,'accounts/customer.html',context)