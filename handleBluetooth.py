#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from termcolor import colored
import api


def check_home(person):
	result = bluetooth.lookup_name(person.bluetooth_address, timeout=5)
	if (result != None):
		if not (person.isPresent()):
			print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + "  " + colored(person.name, person.getColor()) + " has arrived in Paradise!")
			person.setPresence(True)
			api.post_presence(person)

	elif ( person.isPresent() ) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) +"  " + colored(person.name, person.getColor()) + " has left Paradise.")
		person.setPresence(False)
		api.post_presence(person)
