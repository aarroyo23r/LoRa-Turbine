from network import LoRa
import socket
import machine
import time
import os

global i
global identificador
global dato2
global dato1
global linea

i = 0
identificador = 0
dato1 = 0
dato2 = 0
linea = 0

# initialise LoRa in LORA mode
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
# more params can also be given, like frequency, tx power and spreading factor
lora = LoRa(mode=LoRa.LORA)
​
# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
​
while True:

    s.setblocking(False)
    data = s.recv(64)
    identificador = int(data[0:1])


    if identificador == 1 :
        print('Dato sensor 1 ',data[1:])

        f = open('/flash/hola.txt','w')
        f.write ('Dato sensor 1 ')
        f.write (data[1:])
        f.close()

        time.sleep(1)

    elif identificador == 2 :
        print('Dato sensor 2 ', data[1:])
        f = open('/flash/hola.txt','w')
        f.write ('Dato sensor 2 ')
        f.write (data[1:])
        f.close()
        time.sleep(1)

    elif identificador == 3 :
        print('Dato sensor 3 ', data[1:])
        f = open('/flash/hola.txt','w')
        f.write ('Dato sensor 3 ')
        f.write (data[1:])
        f.close()
        time.sleep(1)
    else:
        print('ERROR')
        time.sleep(1)
