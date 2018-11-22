from network import LoRa
import socket
import machine
import time
from machine import Pin
import pycom
import read_rotencods
import read_floras

from machine import I2C
from math import atan2, pi, sqrt

from lib.lsm303 import LSM303D


global i
global medi1
global medi2
global medi3
global medi4
global medi5
global medi6

#Esto debe ir en el MAIN

#Para el primer codificador rotacional
CLK1 = Pin('P8', mode=Pin.IN, pull=None, alt=-1) #Es el pin P8
DT1 = Pin('P11', mode=Pin.IN, pull=None, alt=-1) #Es el pin P11

#Para el segundo codificador rotacional
CLK2 = Pin('P21', mode=Pin.IN, pull=None, alt=-1) #Es el pin P21
DT2 = Pin('P20', mode=Pin.IN, pull=None, alt=-1) #Es el pin P20

#Esto debe ir en el MAIN

#Esto debe ir en el MAIN
i2c1 = I2C(0 , I2C.MASTER, baudrate=100000)  #Conectar un FLORA a pines (P9=SDA, P10=SCL)
lsm303_1 = LSM303D(i2c1)

i2c2 = I2C(1,I2C.MASTER, baudrate=100000, pins=('P23','P22'))     # Conectar el otro FLORA a pines (P23=SDA, P22=SCL)
lsm303_2 = LSM303D(i2c2)
#Esto debe ir en el MAIN

i = 0
medi1 = 1.111
medi2 = 22.2
medi3 = 3333.33333333
medi4 = 444.4444
medi5 = 555
medi6 = 666.6

#pycom.heartbeat(False)
#pycom.rgbled(0xFF0000)  # Red
#time.sleep(1)
#pycom.rgbled(0x00FF00)  # Green
#time.sleep(1)
#pycom.heartbeat(True)

# initialise LoRa in LORA mode
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
# more params can also be given, like frequency, tx power and spreading factor
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
​
# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
​
while True:
    medi1, medi2 = read_floras.READ_FLORA1(lsm303_1)
    medi3, medi4 = read_floras.READ_FLORA2(lsm303_2)


    s.setblocking(True)

    if i < 1:
        s.send('1'+ str(medi1))
        i = i+1

    elif i < 2:
        s.send('2'+ str(medi2))
        i = i+1

    elif i < 3:
        s.send('3'+ str(medi3))
        i = i+1

    elif i < 4:
        s.send('4'+ str(medi4))
        i = i+1

    elif i < 5:
        medi5 = read_rotencods.READ_ROTENCOD1(CLK1, DT1)
        s.send('5'+str(medi5))
        i = i+1

    elif i < 6:
        medi6 = read_rotencods.READ_ROTENCOD2(CLK2, DT2)
        s.send('6'+str(medi6))
        i = i+1

    else:
        i = 0

​
​
    # wait a random amount of time
    time.sleep(0.15)
