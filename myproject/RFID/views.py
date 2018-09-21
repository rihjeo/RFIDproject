from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HUFS")

def log(request):
    return HttpResponse("log list")

def check(request, serialNum):
    num = serialNum
    return HttpResponse(num)
