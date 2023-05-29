#!/usr/bin/python
import time
from bluepy import btle
import sys
import time
import pickle
import binascii

from meater import MeaterProbe
 
print ("Connecting...")
devs = [MeaterProbe(addr) for addr in sys.argv[1:]]
print ("Connected")

while True:
    for dev in devs:
       dev.update()
       print (dev)
    time.sleep(1)
