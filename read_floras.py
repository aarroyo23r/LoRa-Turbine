import pycom
import time
from machine import I2C
from math import atan2, pi, sqrt

from lib.lsm303 import LSM303D

#Esto debe ir en el MAIN
i2c1 = I2C(0 , I2C.MASTER, baudrate=100000)  #Conectar un FLORA a pines (P9=SDA, P10=SCL)
lsm303_1 = LSM303D(i2c1)

i2c2 = I2C(1,I2C.MASTER, baudrate=100000, pins=('P23','P22'))     # Conectar el otro FLORA a pines (P23=SDA, P22=SCL)
lsm303_2 = LSM303D(i2c2)
#Esto debe ir en el MAIN


def READ_FLORAS('''lsm303_1, lsm303_2'''):
    accel1, mag1 = lsm303_1.read()
    x1, y1, z1 = accel1
    roll1 = atan2(y1,z1)*180/pi
    pitch1 = atan2(-x1, sqrt(y1*y1 + z1*z1))*180/pi
    roll_str1 = str(roll1)
    pitch_str1 = str(pitch1)

    accel2, mag2 = lsm303_2.read()
    x2, y2, z2 = accel2
    roll2 = atan2(y2,z2)*180/pi
    pitch2 = atan2(-x2, sqrt(y2*y2 + z2*z2))*180/pi
    roll_str2 = str(roll2)
    pitch_str2 = str(pitch2)

    return (roll_str1, pitch_str1, roll_str2, pitch_str2)
