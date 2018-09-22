import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import urllib.request

lock = False

url = 'http://192.168.0.6:8000'
hdr = {'User-Agent': 'Mozilla/5.0', 'referer' : 'http://192.168.0.6:8000'}
Data = b'qnqnqn, 123'

continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    p.stop()
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(0)
print ("Press Ctrl-C to stop.")

while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        real = ""
        # Print UID
        for i in uid:
            a = str(i)
            real = real + a
        print(real)
        req = requests.get("http://192.168.0.245:8000/check/"+real)
        if req.text == "ok":
            if not lock:
                p.ChangeDutyCycle(1)
                print("angle : 1")
                x = real + " " + "close"
                x = x.encode()
                eq = urllib.request.Request(url=url,data=x,method='PUT',headers=hdr)
                f = urllib.request.urlopen(req)
                print(f.status)
                print(f.reason)
                response = f.read()
                response = response.decode()
                print(response)
                lock = True
            elif lock:
                p.ChangeDutyCycle(8)
                print("angle : 8")
                x = real + " " + "open"
                x = x.encode()
                eq = urllib.request.Request(url=url,data=x,method='PUT',headers=hdr)
                f = urllib.request.urlopen(req)
                print(f.status)
                print(f.reason)
                response = f.read()
                response = response.decode()
                print(response)
                lock = False
            GPIO.output(23,True)
            time.sleep(1)
            GPIO.output(23,False)
        else:
            GPIO.output(24,True)
            time.sleep(1)
            GPIO.output(24,False)
            

