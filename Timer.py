#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(90)
sense.clear()
for i in range(10,-1,-1):
	sense.show_message( str(i) )
	sleep(1)
sense.clear()