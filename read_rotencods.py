from machine import Pin
import pycom
import time

#Constantes Generales
SAMPLE_DELAY = 1
PULSES_PER_TURN = 40

#Esto debe ir en el MAIN

#Para el primer codificador rotacional
CLK1 = Pin('P12', mode=Pin.IN, pull=None, alt=-1) #Es el pin P12
DT1 = Pin('P11', mode=Pin.IN, pull=None, alt=-1) #Es el pin P11

#Para el segundo codificador rotacional
CLK2 = Pin('P21', mode=Pin.IN, pull=None, alt=-1) #Es el pin P21
DT2 = Pin('P20', mode=Pin.IN, pull=None, alt=-1) #Es el pin P20

#Esto debe ir en el MAIN

def READ_ROTENCOD1(#CLK1, DT1#):
    lastTime1 = time.time()
    poscount1 = 0
    CLKLast1 =  CLK1.value() #Leer ultimo valor de CLK1

    while time.time()-lastTime1 <= 1.2:
        state1 = CLK1.value()
        if state1 != CLKlast1:
            if DT1.value() != state1:
                poscount1 = poscount1 + 1
            else:
                poscount1 = poscount1 - 1

        CLKLast1 = state1

        if time.time()-lastTime1 >= SAMPLE_DELAY:
            rpm1 = (poscount1*(60 / (time.time() - lastTime1))) / PULSES_PER_TURN
            poscount1 = 0
            lastTime1 = time.time()
            return (rpm1)



def READ_ROTENCOD2(#CLK2, DT2):
    lastTime2 = time.time()
    poscount2 = 0
    CLKLast2 =  CLK2.value() #Leer ultimo valor de CLK

    while time.time()-lastTime2 <= 1.2:
        state2 = CLK2.value()
        if state2 != CLKlast2:
            if DT2.value() != state2:
                poscount2 = poscount2 + 1
            else:
                poscount2 = poscount2 - 1

        CLKLast2 = state2


        if time.time()-lastTime2 >= SAMPLE_DELAY:
            rpm2 = (poscount2*(60 / (time.time() - lastTime2))) / PULSES_PER_TURN
            poscount2 = 0
            lastTime2 = time.time()
            return (rpm2)
