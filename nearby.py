#!/usr/bin/python

import bluetooth
import time
import os

os.environ["TZ"] = "Europe/Oslo"
time.tzset()


print("""Paradise: Who's home?""")

havard = 0
frederik = 0
raymi = 0
tormod = 0


while True:

	result = bluetooth.lookup_name('40:B8:37:2C:C6:9F', timeout=5)
	if (result != None):
		if (havard == 0):
			print(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + "  Haavard har kommet!")
			havard = 1
		
	elif ( havard == 1) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) +"  Haavard har dratt.")
		havard = 0


	result = bluetooth.lookup_name('F0:24:75:73:CE:7F', timeout=5)
	if (result != None):
		if (frederik == 0):
			print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + "  Frederik har kommet!")
			frederik = 1
	elif (frederik == 1) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + "  Frederik har dratt.")
		frederik = 0

	result = bluetooth.lookup_name('84:8E:DF:4B:D7:9F', timeout=5)
	if (result != None):
		if (raymi == 0):
			print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + "  Raymi har kommet!")
			raymi = 1
	elif (raymi == 1) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + "  Raymi har dratt.")
		raymi = 0

	result = bluetooth.lookup_name('F4:8E:92:7F:27:12', timeout=5)
	if (result != None):
		if (tormod == 0):
			print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + "  Tormod har kommet!")
			tormod = 1
	elif (tormod == 1) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + "  Tormod har dratt.")
		tormod = 0


	time.sleep(2)
