import serial
import time
import subprocess
import os


def serialInit(puerto, baudios=9600, timeout=1):
    return serial.Serial(puerto, baudios, timeout=timeout)


def sim800Response(phone, puerto, mensaje="CMTI"):
    while True:
        try:
            response = str(phone.readline())
            print(response)
            if mensaje in response:             
                break
        except:
            print ("Ha ocurrido una excepcion")
            print ('-'*60)
            subprocess.call(['sudo', 'systemctl', 'stop', 'serial-getty@{}.service'.format("ttyS0")])
    #print(response if response != "b\'\'" else 'error')
    
def ver(phone, puerto): 
    phone.write(str('AT+CMGL="ALL",0\r').encode('utf-8'))
    sim800Response(phone, puerto, mensaje="OK")
mensaje="Hola"
def sms(phone, puerto, mensaje):
    phone.write("AT\r".encode('utf-8'))
    time.sleep(1)
    phone.write("AT+CMGF=1\r\n".encode('utf-8'))
    time.sleep(1)
    phone.write(str('AT+CMGS="+573015733885"\r\n'.encode('utf-8')))
    time.sleep(2)
    phone.write(mensaje+chr(26))
    time.sleep(4)
    print("Mensaje enviado")
    #sim800Response(phone, puerto, mensaje="OK")
    
if (__name__ == '__main__'):
    puerto = "ttyS0"   
    phone = serialInit('/dev/{}'.format(puerto))
    #phone.write(str('AT+CMGF=1\r').encode('utf-8'))
    sms(phone, puerto, mensaje)
    #ver(phone,puerto)
