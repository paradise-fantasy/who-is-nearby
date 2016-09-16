#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from termcolor import colored


def check_home(person):
	result = bluetooth.lookup_name(person.mac, timeout=5)
	if (result != None):
		if not (person.isPresent()):
			print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + "  " + colored(person.name, person.getColor()) + " har ankommet!")
			person.setPresence(True)

	elif ( person.isPresent() ) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) +"  " + colored(person.name, person.getColor()) + " har dratt.")
		person.setPrescence(False)
