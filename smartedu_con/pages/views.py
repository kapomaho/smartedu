from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request,'about.html')
    
def index(request):
    return render(request,'index.html')


# Create your views here.
