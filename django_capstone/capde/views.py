from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

def main(request):
    now = datetime.now()

    context = {
        "now":now
    }
    return render(request,'main/main.html',context)    

def alba_main(request):
    now = datetime.now()

    context = {
        "now":now
    }
    return render(request,'alba_main/alba_main.html',context)

def ceo_main(request):
    now = datetime.now()

    context = {
        "now":now
    }
    return render(request,'ceo_main/ceo_main.html',context)