from network import LoRa
import socket
import machine
import time
import os
import utime


global identificador
global linea
global space
global i

sensor1 = '0'
sensor2 = '0'
sensor3 = '0'
sensor4 = '0'
sensor5 = '0'
sensor6 = '0'
space = ' '
index = 1
i = 0



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

'''
def set_index(outputFile):

    file= open(outputFile,'r')
    text = file.read()
    num_lines = str(text.count("\n") + 1)
    file.close()
    return num_lines

'''

def write_file(sensor1,sensor2,sensor3,sensor4,sensor5,sensor6):


    file = open('/flash/test.txt','a')

    file.write(sensor1)
    file.write('\n')
    file.write(sensor2)
    file.write('\n')
    file.write(sensor3)
    file.write('\n')
    file.write(sensor4)
    file.write('\n')
    file.write(sensor5)
    file.write('\n')
    file.write(sensor6)
    file.write('\n')

    file.close()



​
while True:

    #s.setblocking(False)
    #data = s.recv(64)
    #identificador = int(data[0:1])
    #print(data)
    x = 0

    for x in range(0, 6):
        s.setblocking(False)
        data = s.recv(64)
        time.sleep(0.30)
        identificador = int(data[0:1])
        if identificador == 1 :
            sensor1 = data[1:]
            sensor2 = sensor2
            sensor3 = sensor3
            sensor4 = sensor4
            sensor5 = sensor5
            sensor6 = sensor6
            x = x + 1



        elif identificador == 2 :
            sensor1 = sensor1
            sensor2 = data[1:]
            sensor3 = sensor3
            sensor4 = sensor4
            sensor5 = sensor5
            sensor6 = sensor6
            x = x + 1


        elif identificador == 3 :
            sensor1 = sensor1
            sensor2 = sensor2
            sensor3 = data[1:]
            sensor4 = sensor4
            sensor5 = sensor5
            sensor6 = sensor6
            x = x + 1



        elif identificador == 4 :
            sensor1 = sensor1
            sensor2 = sensor2
            sensor3 = sensor3
            sensor4 = data[1:]
            sensor5 = sensor5
            sensor6 = sensor6
            x = x + 1



        elif identificador == 5 :
            sensor1 = sensor1
            sensor2 = sensor2
            sensor3 = sensor3
            sensor4 = sensor4
            sensor5 = data[1:]
            sensor6 = sensor6
            x = x + 1



        elif identificador == 6 :
            sensor1 = sensor1
            sensor2 = sensor2
            sensor3 = sensor3
            sensor4 = sensor4
            sensor5 = sensor5
            sensor6 = data[1:]
            x = x + 1


        #time.sleep(0.15)
    os.remove('/flash/test.txt')
    write_file(sensor1,sensor2,sensor3,sensor4,sensor5,sensor6)

    '''
    if identificador == 1 :
        sensor1 = data[1:]
        sensor2 = sensor2
        sensor3 = sensor3
        sensor4 = sensor4
        sensor5 = sensor5
        sensor6 = sensor6


    elif identificador == 2 :
        sensor1 = sensor1
        sensor2 = data[1:]
        sensor3 = sensor3
        sensor4 = sensor4
        sensor5 = sensor5
        sensor6 = sensor6


    elif identificador == 3 :
        sensor1 = sensor1
        sensor2 = sensor2
        sensor3 = data[1:]
        sensor4 = sensor4
        sensor5 = sensor5
        sensor6 = sensor6


    elif identificador == 4 :
        sensor1 = sensor1
        sensor2 = sensor2
        sensor3 = sensor3
        sensor4 = data[1:]
        sensor5 = sensor5
        sensor6 = sensor6


    elif identificador == 5 :
        sensor1 = sensor1
        sensor2 = sensor2
        sensor3 = sensor3
        sensor4 = sensor4
        sensor5 = data[1:]
        sensor6 = sensor6


    elif identificador == 6 :
        sensor1 = sensor1
        sensor2 = sensor2
        sensor3 = sensor3
        sensor4 = sensor4
        sensor5 = sensor5
        sensor6 = data[1:]



    write_file(sensor1,sensor2,sensor3,sensor4,sensor5,sensor6)




    time.sleep(1)
    '''
