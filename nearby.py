#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time

print("""Paradise: Who's home?""")

class Person:
	def __init__(self, name, mac):
		bluetoothPrescence = False
		self.name = name
		self.mac = mac
	def isPresent():
		return bluetoothPresence
	def setPrescence(prescence):
		self.bluetoothPresence = prescence


havard		=	Person("Håvard",		"40:B8:37:2C:C6:9F")
frederik	=	Person("Frederik",		"F0:24:75:73:CE:7F")
raymi		=	Person("Raymi",			"84:8E:DF:4B:D7:9F")
tormod		=	Person("Tormod",		"F4:8E:92:7F:27:12")
kabbe		=	Person("Jon-Anders",	"F4:8E:92:7F:27:10")

alle = [havard, frederik, raymi, tormod, kabbe]



def check_home(person):
	result = bluetooth.lookup_name(person.mac, timeout=5)
	if (result != None):
		if not (person.isPresent()):
			print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + "  " + person.name + " har ankommet!")
			person.setPresence(True)

	elif ( person.isPresent() ) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) +"  " + person.name + " har dratt.")
		person.setPrescence(False)


while True:

	for person in alle:
		check_home(person)

	time.sleep(2)
