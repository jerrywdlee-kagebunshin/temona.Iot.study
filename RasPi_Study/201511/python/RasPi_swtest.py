# -*- coding: utf-8 -*-
#client.py
import time
import RPi.GPIO as GPIO
INPUT_IO = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_IO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print "=" *20
print "Temona SW Test "
print "=" *20
print
print "Exit ->  Ctrl+C"
print

while 1:
    print GPIO.input(INPUT_IO) 
    if GPIO.input(INPUT_IO) !=1 :
        print "Push ON !!"
       
    time.sleep(0.1)