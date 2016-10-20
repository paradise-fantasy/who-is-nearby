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
			print(timestamp() + colored(person.name, person.getColor()) + " has arrived in Paradise!")
			person.setPresence(True)
			api.post_presence(person)
			send_presence_event(str(str(person.name) + " has arrived in " + str(person.room)))

	elif ( person.isPresent() ) :
		print( timestamp() + colored(person.name, person.getColor()) + " has left Paradise.")
		person.setPresence(False)
		api.post_presence(person)
		send_presence_event(str(str(person.name) + " has left " + str(person.room)))
