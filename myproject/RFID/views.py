from django.shortcuts import render
from .models import RfidDB
<<<<<<< HEAD
from .models import Status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "PUT" or "GET":
        #try:
        message = request.read()
        message = message.decode()
        info = message.split(" ")
        mserial, mstatus = info[0],info[1]
        statusDB = Status.objects.get(serial = mserial)
        statusDB.status = mstatus
        statusDB.save()

        now = datetime.now()
        timeData = '%s-%s-%s %s:%s:%s' % ( now.year, now.month, now.day, now.hour, now.minute, now.second )

        rfidData = RfidDB(serial = mserial, status = mstatus, time = timeData)
        rfidData.save()

        #except:
        #    rfidData = None
        #    statusData = None
        #    return HttpResponse("u")
        return HttpResponse("Modify")
def status(request):
    statusDB = Status.objects.all()
    str = ''
    for s in statusDB:
        str += "SerialNum {} Status {}<br>".format(s.serial, s.status)
    return HttpResponse(str)
=======
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
>>>>>>> b977d037f2f5ca8f5f686e8c79e1ffe490139d88

        except:
            rfiddatas = None
        return HttpResponse("modify")
def log(request):
    rfidDB = RfidDB.objects.all()
    str = ''
    for log in rfidDB:
<<<<<<< HEAD
        str += "SerialNum {} Status {} Time {}<br>".format(log.serial, log.status, log.time)
=======
        str += "SerialNum {} Status {}<br>".format(log.serial, log.status)
>>>>>>> b977d037f2f5ca8f5f686e8c79e1ffe490139d88
    return HttpResponse(str)


def check(request, serialNum):
<<<<<<< HEAD
    statusDB = Status.objects.all()
    ser = []
    serialNum = int(serialNum)
    for s in statusDB:
        ser.append(s.serial)
=======
    rfidDB = RfidDB.objects.all()
    ser = []
    serialNum = int(serialNum)
    for log in rfidDB:
        ser.append(log.serial)
>>>>>>> b977d037f2f5ca8f5f686e8c79e1ffe490139d88
    if serialNum in ser:
        return HttpResponse("ok")
    else:
        return HttpResponse("no")
<<<<<<< HEAD

def test(request):
    statusDB = Status.objects.get()
=======
>>>>>>> b977d037f2f5ca8f5f686e8c79e1ffe490139d88
