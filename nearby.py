#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from Person import Person
from handleBluetooth import check_home
import api
import logging
from termcolor import colored
from mqtt_api import send_everyone_present

logging.basicConfig(filename='/home/pi/who-is-nearby/logs/output.log', level=logging.DEBUG)

list_of_members = api.get_members()
currently_home_paradise = 0

def main():
	kick_everyone_out()
	logging.info("[*] Paradise: Who's home?")
	while True:

		for person in list_of_members:
			check_home(person)
		counter = 0
		for deltager in list_of_members:
			if (deltager.isPresent() and deltager.room == "paradise"):
				counter += 1
		if (counter == 4 && currently_home_paradise != 4):
			send_everyone_present("true")
		currently_home_paradise = counter

		time.sleep(2)

def kick_everyone_out():
	logging.info("[*] Kicking everyone out.")
	for person in list_of_members:
		#if person.isPresent():
		person.setPresence(False)
		api.post_presence(person)
		logging.info("[*] " + person.name + " was kicked out.")
		print(colored(person.name, person.color) + " was kicked out.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		kick_everyone_out()
		logging.info("[*] Shutting down.")
