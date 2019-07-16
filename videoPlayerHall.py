#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
import sys
from subprocess import Popen
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(17, GPIO.IN)

movie1 = ("/home/pi/Desktop/movie1.mp4")
 
print("------------------")
print(" OMXPlayer + GPIO ")
print("------------------")
 
print("--------------")
#print GPIO.input(17)
print("--------------")

while True:
        #Read states of inputs
        input_state1 = GPIO.input(17)

        if ( input_state1 == False ):
            print("Button Pressed")
            #os.system('omxplayer -b movie1 &')
            omxc = Popen(['omxplayer', '-b', movie1])
            sleep(15)
            input_state1 = True
