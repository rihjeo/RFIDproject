#https://github.com/mxgxw/MFRC522-python/blob/master/MFRC522.py
import urllib.request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(0)
time.sleep(1)

lock = True

url = 'http://192.168.0.6:8000'
hdr = {'User-Agent': 'Mozilla/5.0', 'referer' : 'http://192.168.0.6:8000'}
Data = b'111 close'

req = urllib.request.Request(url=url,data=Data,method='PUT',headers=hdr)
f = urllib.request.urlopen(req)

print(f.status)
print(f.reason)
response = f.read()
response = response.decode()
print(response)

if response == "as":
    if not lock:
        p.ChangeDutyCycle(1)
        print("angle : 1")
        lock = True
    elif lock:
        p.ChangeDutyCycle(8)
        print("angle : 8")
        lock = False
    GPIO.output(23,True)
    time.sleep(1)
    GPIO.output(23,False)
else:
    GPIO.output(24,True)
    time.sleep(1)
    GPIO.output(24,False)
p.stop()
GPIO.cleanup()