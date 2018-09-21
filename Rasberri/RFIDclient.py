import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import requests


continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

print ("Press Ctrl-C to stop.")

while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        real = ""
        # Print UID
        for i in uid:
            a = str(i)
            real = real + a
        req = requests.get(http://)
    
