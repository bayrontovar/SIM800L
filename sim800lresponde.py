import serial
import time

phone = serial.Serial("/dev/ttyS0", 9600, timeout=1)

def sim800_responde():
    while True:
        response = str(phone.readline())    
        if "CMTI" in response:
            print("OK")
            break
    print(response if response != "b\'\'" else 'error')   
sim800_responde()
