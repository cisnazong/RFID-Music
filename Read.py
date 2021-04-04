from time import sleep
import sys
import argparse
from pythonosc import udp_client
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import os
import Switcher

# 电源改为GPIO口，由继电器控制


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
                    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5555,
                    help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

volume = 98  # 初始化音量

os.system("amixer set Headphone " + str(volume) + "%")

res = 0
idl = []

idl = [1007583446930, 109359453160, 484757090905, 789524923514]
i = 0
j = 0
time_interval = 0.03
resl = [0, 0, 0, 0]

try:
    while True:
        sleep(0.01)
        # 继电器 No. i 接通，/boxi准备输出
        reader = SimpleMFRC522()
        # print("Hold a tag near the reader")
        # sleep(0.01)
        id, text = reader.read(time_interval)
        # print('id is : ',id) #if id == None: no return, thus res = 0
        if id is None:
            resl[i] = 0
        else:
            if id in idl:
                continue
            else:
                idl.append(id)
                resl.append(0)
        # print('res is : ',res)
        #
        #    continue
        # else:
        #    idl.append()
        ##
        ############
        # id = idl[i]#
        ############
        # print("ID: %s\nText: %s" % (id,text))
        if id in idl:
            res = list.index(id) + 1
            resl[i] = res
        else:
            res = 0
            resl[i] = 0

        #        if id == idl[0]:
        #            res = 1
        #        elif id == idl[1]:
        #            res = 2
        #        elif id == idl[2]:
        #            res = 3
        #        elif id == idl[3]:
        #            res = 4
        #        else:
        #            res = 0

        boxid = "/box" + str(i)
        client.send_message(boxid, res)

        #        client.send_message("/box1", res)
        #        client.send_message("/box2", res)
        #        client.send_message("/box3", res)
        #        client.send_message("/box4", res)

        # client.send_message("/box1", res)
        # client.send_message("/box2", res)
        # client.send_message("/box3", res)
        # client.send_message("/box4", res)
        client.send_message("/stop", '---')
        ########
        i = i + 1  #
        ########
        print('send: ', res)
        print('resl: ', resl)
        if i >= len(idl):
            i = 0
            j = j + 1
            # print(i)

        # 设置音量
        if sum(resl) == 0:
            os.system("amixer set Headphone 0%")
        else:
            os.system("amixer set Headphone " + str(volume) + "%")
        for ii in range(len(resl)):
            resl[ii] = 0

        # 继电器 No. i 关闭

except KeyboardInterrupt:
    GPIO.cleanup()
    raise
