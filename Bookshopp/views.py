from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def mybook(request):
    return render(request,'mybook.html')

def iphone(request):
    return render(request,'iphone.html')

def food(request):
    return render(request,'food.html')