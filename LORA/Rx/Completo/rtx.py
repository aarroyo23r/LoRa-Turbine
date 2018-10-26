#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals, print_function
 
import time
import os
import sys
import tty, termios
import _thread

space=' '


def prom_data(sensorDirection,samples):
    sensor = [0] * samples
    sensor_prom=0
    for i in range(0, samples):
	try:
		s1= open(sensorDirection,'r')
		sensor[i]=s1.read()
		sensor_prom= sensor_prom + int(sensor[i])
        except:
                print ('Reading error in the measure '+ str(i))
		sensor_prom=-1

    sensor_prom=str(sensor_prom/samples)
    return  sensor_prom

def new_file (outputFile):
    os.remove(outputFile)
    file = open(outputFile,'w') 
    file.write('idx   date     time  sensor 1 \n')
    file.close()


def write_file(sensor1_prom,sensor2_prom,sensor3_prom,outputFile):

    index=set_index(outputFile)
    date=time.strftime('%d/%m/%Y ')
    hour=time.strftime('%I:%M%p')


    file = open(outputFile,'a') 

    file.write(index+space)  
    file.write(date) 
    file.write(hour)
    file.write(space+sensor1_prom) 
    file.write(space+sensor2_prom) 
    file.write(space+sensor3_prom)  
    file.write(space+sensor4_prom+'\n')  

    file.close() 


def set_index(outputFile):
    file= open(outputFile,'r')
    text = file.read()
    num_lines = str(text.count("\n") + 1)
    file.close()
    return num_lines



def getch():   
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
 

    
 
