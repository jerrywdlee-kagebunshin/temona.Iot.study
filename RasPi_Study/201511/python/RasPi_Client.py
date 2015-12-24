# -*- coding: utf-8 -*-
#client.py
import time
import json
import random
import requests
import argparse
import commands

import RPi.GPIO as GPIO
INPUT_IO = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_IO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#==================================================#
if __name__ == "__main__":

    print "=" *20
    print "Temona Call Test Client"
    print "=" *20
    print
    print "Exit ->  Ctrl+C"
    print

    #url = raw_input("URL? (http://?)= ")
    url = "http://192.168.110.2:8080/hw/api"
    devid = raw_input("DebID? (xxxxxx)= ")
    print url
    print devid
    cnt = 0
    data = {}
    data['devid'] = devid
    data['url'] = url
    data['SW1'] = ""
    data['time'] = ""
    data['cnt'] = 0
    data['service'] = "switch"
    print "Pleas Push!"
    import datetime
    while 1:
            now = datetime.datetime.today()
            #print "Pleas Puss!"
	    if(GPIO.input(INPUT_IO) !=1):
                sw1 = 1
                print "Push ON !!"
                print "注文が送信されました。"
            else :
                sw1 = 0
            data['SW1'] = sw1
            data['time'] = now.strftime("%H:%M:%S")
            data['cnt'] = cnt
            print json.dumps(data)
            cnt = cnt+1
            r = requests.get(url,data=json.dumps(data))
            time.sleep(0.5)
            #print r.text
            print "Pleas Push!"
    #exit()
