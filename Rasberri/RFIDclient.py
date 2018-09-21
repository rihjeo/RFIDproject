import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import requests

lock = False

continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
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
        print("1")
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        real = ""
        # Print UID
        for i in uid:
            a = str(i)
            real = real + a
        print(real)
        req = requests.get("http://192.168.0.245:8000")
        if req.text == "HUFS":
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
            
    
