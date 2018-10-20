import pycom
import time
from machine import I2C
from math import atan2, pi, sqrt


from lib.lsm303 import LSM303D
i2c = I2C(0,I2C.MASTER, baudrate=100000)
devices = i2c.scan()
lsm303 = LSM303D(i2c)

print(devices)
while True:
    accel, mag = lsm303.read()
    x, y, z = accel
    h = atan2(y, x) * 180.0 / pi
    w = abs(int(h))
    roll = atan2(y,z)*180/pi
    pitch = atan2(-x, sqrt(y*y + z*z))*180/pi

    roll_str = str(roll)
    pitch_str = str(pitch)

    print("Cambio de angulo en eje x: %s" %(roll_str))
    print("\n")
    print("Cambio de angulo en eje y: %s" %(pitch_str))
    print("\n")

    time.sleep(1)
