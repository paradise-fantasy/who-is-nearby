#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from termcolor import colored
import api
from mqtt_api import send_presence_event

def timestamp():
	return "[" + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + "] "


def check_home(person):
	result = bluetooth.lookup_name(person.bluetooth_address, timeout=5)
	if (result != None):
		if not (person.isPresent()):
			print(timestamp() + colored(person.name, person.getColor()) + " has arrived in " + person.room)
			person.setPresence(True)
			send_presence_event(str(str(person.name) + " has arrived in " + str(person.room)))

	elif ( person.isPresent() ) :
		print( timestamp() + colored(person.name, person.getColor()) + " has left " + person.room)
		person.setPresence(False)
		person.last_present = time.localtime()
		send_presence_event(str(str(person.name) + " has left " + str(person.room)))
