#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from Person import Person
from handleBluetooth import check_home
import api
from termcolor import colored


list_of_members = api.get_members()

def main():
	print("""Paradise: Who's home?""")
	while True:

		for person in list_of_members:
			check_home(person)

		time.sleep(2)

def kick_everyone_out():
	for person in list_of_members:
		if person.isPresent():
			person.setPresence(False)
			api.post_presence(person)
			print(colored(person.name, person.color) + " was kicked out.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Kicking everyone out.")
		kick_everyone_out()
		print("Shutting down.")
