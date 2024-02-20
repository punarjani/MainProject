from django.shortcuts import render
from .models import *
# Create your views here.


def first(request):
    return render(request,"first.html")
def form(request):
    sum=""
    if "add" in request.POST:
        f=int(request.POST['first'])
        s=int(request.POST['second'])
        sum=f+s
        print(sum)
    elif "sub" in request.POST:
        f=int(request.POST['first'])
        s=int(request.POST['second'])
        sum=f-s
    elif "mul" in request.POST:
        f=int(request.POST['first'])
        s=int(request.POST['second'])
        sum=f*s
    elif "div" in request.POST:
        f=int(request.POST['first'])
        s=int(request.POST['second'])
        sum=f/s
    return render(request,"form.html",{"sum":sum})
def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def useradd(request):
    return render(request,"UserAdd.html")
    
