import os
import time
import smbus
from socket import *
bus = smbus.SMBus(1)
BROADCAST_TO_PORT = 7000

bus.write_byte(0x48, 0x02)

last_reading = -1

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    tempreading = bus.read_byte(0x48)
    tempreading = bus.read_byte(0x48)
    if (abs(last_reading - tempreading) > 2):
        data = "temp " + str(tempreading)
        s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
        print(data)
        time.sleep(1)
