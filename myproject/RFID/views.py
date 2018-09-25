from django.shortcuts import render
from .models import RfidDB
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

def log(request):
    rfidDB = RfidDB.objects.all()
    str = ''
    for log in rfidDB:
        str += "SerialNum {} Status {} Time {}<br>".format(log.serial, log.status, log.time)
    return HttpResponse(str)

def check(request, serialNum):
    statusDB = Status.objects.all()
    ser = []
    serialNum = int(serialNum)
    for s in statusDB:
        ser.append(s.serial)
    if serialNum in ser:
        return HttpResponse("ok")
    else:
        return HttpResponse("no")

def test(request):
    statusDB = Status.objects.get()
