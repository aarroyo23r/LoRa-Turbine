from network import LoRa
import socket
import machine
import time
from collections import deque
​
global i
global medi1
global medi2
global medi3
global medi4
global medi5
global medi6

i = 0
medi1 = 1.111
medi2 = 22.2
medi3 = 3333.33333333
medi4 = 444.4444
medi5 = 555
medi6 = 666.6

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

    s.setblocking(True)

    if i < 1:
        s.send('1'+str(medi1))
        i = i+1

    elif i < 2:
        s.send('2'+str(medi2))
        i = i+1

    elif i < 3:
        s.send('3'+str(medi3))
        i = i+1

    elif i < 4:
        s.send('4'+str(medi4))
        i = i+1

    elif i < 5:
        s.send('5'+str(medi5))
        i = i+1

    elif i < 6:
        s.send('6'+str(medi6))
        i = i+1

    else:
        i = 0

​
​
    # wait a random amount of time
    time.sleep(0.15)
