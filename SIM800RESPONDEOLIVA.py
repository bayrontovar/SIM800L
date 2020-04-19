import serial
import time


# phone = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
def serialInit(puerto, baudios=9600, timeout=1):
    return serial.Serial(puerto, baudios, timeout=timeout)

def sim800Response(phone):
    while True:
        response = phone.readline()
        print(response)
        # break if 'OK'.lower() in response.lower() else pass
        if( "OK" in response ):
            break

if __name__ == '__main__':
    phone = serialInit("/dev/ttyS0")
    sim800Response(phone)
