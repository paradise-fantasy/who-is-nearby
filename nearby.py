#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from Person import Person
from handleBluetooth import check_home
import api
import logging
from termcolor import colored

logging.basicConfig(filename='home/pi/who-is-nearby/logs/output.log', level=logging.DEBUG)

list_of_members = api.get_members()

def main():
	kick_everyone_out()
	logging.debug("[*] Paradise: Who's home?")
	while True:

		for person in list_of_members:
			check_home(person)

		time.sleep(2)

def kick_everyone_out():
	for person in list_of_members:
		if person.isPresent():
			person.setPresence(False)
			api.post_presence(person)
			logging.debug("[*] " + person.name + " was kicked out.")
			print(colored(person.name, person.color) + " was kicked out.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		logging.debug("[*] Kicking everyone out.")
		kick_everyone_out()
		logging.debug("[*] Shutting down.")
