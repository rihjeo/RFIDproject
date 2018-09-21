from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RfidDB
import json

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "PUT":
        rfidDB = RfidDB.objects.all()
        context = {'rfidData' : rfidDB}
        try:
            massage = str(request.read())
            info = massage.split(",")
            mname , mserial = info[0] , info[1]
            data = RfidDB(name=mname, serial=mserial)
            data.save()
        except:
            data = None
    return HttpResponse(massage)

def log(request):
    rfidDB = RfidDB.objects.all()
    str = ''
    for log in rfidDB:
        str += "Name {} SerialNum {}<br>".format(log.name, log.serial)
    return HttpResponse(str)

def check(request, serialNum):
    num = serialNum
    return HttpResponse(num)
