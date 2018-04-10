import serial
import paho.mqtt.client as mqtt
import string
import sys

import time
import datetime
import json
import binascii
import base64

# python script that counts to 10 by passing a value between the xDot and the pivot server

# there are two 'clients' - one is the xDot and one is the python script (via an MQTT client)

# global variables
network = "pivot.iuiot.org"


pl1 = "{\"data\":\""
pl2 = "\",\"deveui\":\"00-80-00-00-04-00-51-87\"}"


pivread = True

#pivot client stuff
def on_message(client, userdata, msg):
    pl = ""
    # for s in msg.payload:
    #     pl += binascii.b2a_qp(s)
    # dj = json.dumps(pl)
    # js = json.load(dj)
    info = base64.b64decode(json.loads(msg.payload)['data'])
    p,t = info.split("&")
    dump = open("./pandt.txt",mode='a+')
    tm = time.ctime()
    dump.write('\n' + tm)
    dump.write("\npressure = " + str(p))
    dump.write("\ntemperature = " + str(t))
    #print('temp  = ' + str(t))
    #print('pressure = ' + str(p))
    dump.close()


MTAyNiYwLjAw
pivot = mqtt.Client()
pivot.on_message = on_message
pivot.connect(network)
pivot.subscribe("lora/00-80-00-00-04-00-51-87/up")
pivot.loop_forever()

def test():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    print(ser.name)
    pivot.loop_start()
    while 1:
        print('testing...')
        time.sleep(2)
        ser.write('s')
    print('something is very wrong')

def measure():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    print(ser.name)
    pivot.loop_start()
    hrs = 0
    while hrs < 49:
        print('measuring data')
        time.sleep(3600)
    print('measuring finished')
    pivot.loop_stop()

# def count():
#     global counter
#     counter = 0
#     pivot.loop_start()
#     while counter < 11:
#         print dots + str(counter)
#         xret = (xd.send_message(str(counter))).decode()
#         #counter+=1
#         if xret != "":
#             rec = int(xret)
#         else:
#             rec = -1
#         if rec > 0:
#             print dotr + str(rec)
#             global counter
#             counter = rec
#             counter+=1
#         # if pivread:
#             # pivot.publish("lora/00-80-00-00-04-00-51-87/down", str(counter))
#             # print pivd + str(counter)
#             # global pivread
#             #pivread = False
#     pivot.loop_stop()
#     print "finished"
