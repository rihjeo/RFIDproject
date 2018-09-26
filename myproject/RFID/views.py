from django.shortcuts import render
from .models import RfidDB
from .models import Status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "PUT":
        try:
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

        except:
            rfidData = None
            statusData = None
            return HttpResponse("u")
        return HttpResponse("Modify")
    elif request.method == "GET":
        return render(request, 'index.HTML')
def status(request):
    statusDB = Status.objects.all()
    context = {'statusDB' : statusDB}
    return render(request, 'status.HTML', context)

def log(request):
    rfidDB = RfidDB.objects.all()
    context = {'rfidDB' : rfidDB}
    return render(request, 'log.HTML', context)

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
