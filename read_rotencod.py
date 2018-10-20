from machine import Pin
import pycom
import time

CLK = Pin('P12', mode=Pin.IN, pull=None, alt=-1) #Es el pin P12
DT = Pin('P11', mode=Pin.IN, pull=None, alt=-1) #Es el pin P12
SAMPLE_DELAY = 1000
PULSES_PER_TURN = 40
poscount = 0
lastTime = 0

CLKLast =  CLK.value() #Leer ultimo valor de CLK

while True:
    state = CLK.value()
    if state != CLKLast:
        if DT.value() != state:
            poscount = poscount + 1
        else:
            poscount = poscount - 1
        print(poscount)
    else:
        print ("No ha cambiado el estado")

    if time.ticks()-lastTime >= SAMPLE_DELAY:
        rpm = (poscount*(60000/ (time.ticks() - lastTime))) / PULSES_PER_TURN))
        poscount = 0
        lastTime = time.ticks()
        print(rpm)
        
    CLKLast = state
