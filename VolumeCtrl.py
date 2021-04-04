import os
from time import sleep

os.system("amixer set Headphone 100%")

for i in range(45):
    volume = 100 - i
    sleep(1)
    cmd = "amixer set Headphone " + str(volume) + "%"
    os.system(cmd)