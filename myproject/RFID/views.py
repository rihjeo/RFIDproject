from django.shortcuts import render
from .models import RfidDB
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "PUT":
        try:
            message = request.read()
            message = message.decode()
            info = message.split(" ")
            mserial, mstatus = info[0],info[1]
            rfidData = RfidDB.objects.get(serial = mserial)
            rfidData.status = mstatus
            rfidData.save()
            # rfiddatas = RfidDB(serial=mserial,status=mstatus)

        except:
            rfiddatas = None
        return HttpResponse("modify")
def log(request):
    rfidDB = RfidDB.objects.all()
    str = ''
    for log in rfidDB:
        str += "SerialNum {} Status {}<br>".format(log.serial, log.status)
    return HttpResponse(str)


def check(request, serialNum):
    rfidDB = RfidDB.objects.all()
    ser = []
    serialNum = int(serialNum)
    for log in rfidDB:
        ser.append(log.serial)
    if serialNum in ser:
        return HttpResponse("ok")
    else:
        return HttpResponse("no")
