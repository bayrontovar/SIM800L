import serial
import time
import subprocess
import os

phone = serial.Serial("/dev/ttyS0", 9600, timeout=1)

def sim800_responde():
    while True:
        try:
            response = str(phone.readline())
            if "CMTI" in response:
                print("OK")
                break
        except:
            print ("Ah ocurrido una excepcion")
            print ('-'*60)
            os.system('sudo systemctl stop serial-getty@ttyAMA0.service')
    print(response if response != "b\'\'" else 'error')   
sim800_responde()
