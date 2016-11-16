#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from Person import Person
from handleBluetooth import check_home
import api
import logging
from termcolor import colored
from mqtt_api import send_everyone_present, send_members_status
import json

logging.basicConfig(filename='/home/pi/who-is-nearby/logs/output.log', level=logging.DEBUG)

list_of_members = api.get_members()
print list_of_members
currently_home_paradise = 0

def main():
	members_status = []
	logging.info(timestamp() + "Paradise: Who's home?")
	while True:
		for person in list_of_members:
			check_home(person)
		counter = 0
		for deltager in list_of_members:
			if (deltager.isPresent() and deltager.room == "paradise"):
				counter += 1
		if (counter == 5 and currently_home_paradise != 5):
			send_everyone_present()
		currently_home_paradise = counter

		new_members_status = [{person.name: person.isPresent()} for person in list_of_members];
		if (json.dumps(members_status) != json.dumps(new_members_status)):
			members_status = new_members_status;
			send_members_status(json.dumps({ "status": members_status }));

		time.sleep(2)

def timestamp():
	return "[" + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + "] "

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		logging.info("[*] Shutting down.")
