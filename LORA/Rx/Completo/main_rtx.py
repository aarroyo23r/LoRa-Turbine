#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
 

from network import LoRa
import socket
import machine

import sys
import tty, termios
import rtx
import time
import _thread
import os



def get_parser():
    """Get parser object for script main_rtx.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-s","--samples",
                        dest="samples",
                        default=1,
                        type=int,
                        help="Number of samples")

    parser.add_argument("-ts","--samplePeriod",
                        dest="samplePeriod",
                        default=1,
                        type=int,
                        help="Sample period in seconds ")

    parser.add_argument("-o","--outputFile",
                        dest="outputFile",
                        default='testRx.txt',
                        type=str,
                        help="Output file name ")

    parser.add_argument("-s1","--sensor1",
                        dest="sensor1",
                        default='/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq',
                        type=str,
                        help="Sensor 1 direction ")

    parser.add_argument("-n","--new",
                        dest="newOutputFile",
                        default='true',
                        type=str,
                        help="Create a new output file and eliminate the old file ")
    return parser



def keypress():
    global char
    char = rtx.getch()

    

def key_detect(char):
    
	    if char is not None:
		_thread.start_new_thread(keypress, ())
		if char == 'q' or char == '\x1b':  # x1b is ESC
		    exit()
		elif (char == 'r'):  # x1b is ESC
		    run="r"
		elif (char == 'p'):  # x1b is ESC
		    run="p"
		char = None


def test(char): 
    run=char

    s.setblocking(False)
    data = s.recv(64)
    identificador = int(data[0:1])

    if (run=="r"):
	    #Sensor 1 Prom
	    #sensor1_prom=rtx.prom_data(args.sensor1,args.samples)
	    if identificador == 1 :
	    	sensor1_prom=data[1:];

	    elif identificador == 2 :
	    	sensor2_prom=data[1:];

            elif identificador == 3 :
	    	sensor3_prom=data[1:];

	    elif identificador == 4 :
	    	sensor4_prom=data[1:];

	    #Write values in output file
	    rtx.write_file(sensor1_prom,sensor2_prom,sensor3,sensor4_prom_promargs.outputFile)


    	    print ("New inserted value  "+ time.strftime('%d/%m/%Y ') +time.strftime('%I:%M%p')+"\n")

    elif (run=="p"):
            os.system("clear")
    	    print ("Press r to continue or q to exit")




if __name__ == "__main__":
    args = get_parser().parse_args()

    lora = LoRa(mode=LoRa.LORA)
    # create a raw LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    global char
    char = None
    run="r"
    
    _thread.start_new_thread(keypress, ())


    os.system("clear")
    print ("Press r to start, p to pause or q to exit")

    while True:
    	key_detect(char)
        test(char)
        time.sleep(args.samplePeriod)

    if (args.newOutputFile=='true'):
	rtx.new_file(args.outputFile)  
    
    
    
    

	

    
    



