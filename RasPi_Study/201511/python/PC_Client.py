# -*- coding: utf-8 -*-
#client.py
import time
import json
import random
import requests
import argparse



#==================================================#
if __name__ == "__main__":

    print "=" *20
    print "Temona Call Test Client"
    print "=" *20
    print
    print "Exit ->  Ctrl+C"
    print

    #url = raw_input("URL? (http://?)= ")
    url = "http://192.168.11.6:8080/hw/api"
    devid = raw_input("DebID? (xxxxxx)= ")
    print devid
    print url
    cnt = 0
    data = {}
    data['devid'] = devid
    data['url'] = url
    data['SW1'] = ""  
    data['SW2'] = ""  
    data['SW3'] = ""  
    data['SW4'] = ""  
    data['time'] = ""
    data['cnt'] = 0
    
    import datetime
    while 1:
            now = datetime.datetime.today()
            tmps = raw_input("How  SW ON? [1 - 4] (bit)= ")
            if(tmps=="0"): 
                (sw1,sw2,sw3,sw4)=("0","0","0","0")
            if(tmps=="1"): 
                (sw1,sw2,sw3,sw4)=("1","0","0","0")
            if(tmps=="2"): 
                (sw1,sw2,sw3,sw4)=("0","1","0","0")
            if(tmps=="3"): 
                (sw1,sw2,sw3,sw4)=("1","1","0","0")
            if(tmps=="4"): 
                (sw1,sw2,sw3,sw4)=("0","0","1","0")
            if(tmps=="5"): 
                (sw1,sw2,sw3,sw4)=("1","0","1","0")
            if(tmps=="6"): 
                (sw1,sw2,sw3,sw4)=("0","1","1","0")
            if(tmps=="7"): 
                (sw1,sw2,sw3,sw4)=("1","1","1","0")
            if(tmps=="8"): 
                (sw1,sw2,sw3,sw4)=("0","0","0","1")
            if(tmps=="9"): 
                (sw1,sw2,sw3,sw4)=("1","0","0","1")
            if(tmps=="10"): 
                (sw1,sw2,sw3,sw4)=("0","1","0","1")
            if(tmps=="11"): 
                (sw1,sw2,sw3,sw4)=("1","1","0","1")
            if(tmps=="12"): 
                (sw1,sw2,sw3,sw4)=("0","0","1","1")
            if(tmps=="13"): 
                (sw1,sw2,sw3,sw4)=("1","0","1","1")
            if(tmps=="14"): 
                (sw1,sw2,sw3,sw4)=("0","1","1","1")
            if(tmps=="15"): 
                (sw1,sw2,sw3,sw4)=("1","1","1","1")

            data['SW1'] = sw1  
            data['SW2'] = sw2  
            data['SW3'] = sw3  
            data['SW4'] = sw4  
            data['time'] = now.strftime("%H:%M:%S")
            data['cnt'] = cnt
            print json.dumps(data)
            cnt = cnt+1
            if(url !=""):
                r = requests.get(url,data=json.dumps(data))
                time.sleep(1)
                print r.text
            time.sleep(1)

        
        #exit()
