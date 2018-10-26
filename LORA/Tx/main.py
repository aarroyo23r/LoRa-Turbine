from network import LoRa
import socket
import machine
import time
​
global i
global medi1
global medi2
global medi3
i = 0
medi1 = 1.111
medi2 = 22.2
medi3 = 3333.33333333

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

    if i < 10:
        s.send('1'+str(medi1))
        i = i+1

    elif i < 20:
        s.send('2'+str(medi2))
        i = i+1

    elif i < 30:
        s.send('3'+str(medi3))
        i = i+1

    else:
        i = 0

​
​
    # wait a random amount of time
    #time.sleep(1)
