#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from Person import Person
from handleBluetooth import check_home
import api


# havard		=	Person("Håvard",		"40:B8:37:2C:C6:9F", 	"blue")
# frederik	=	Person("Frederik",		"F0:24:75:73:CE:7F",	"green")
# raymi		=	Person("Raymi",			"84:8E:DF:4B:D7:9F",	"red")
# tormod		=	Person("Tormod",		"F4:8E:92:7F:27:12",	"yellow")
# kabbe		=	Person("Jon-Anders",		"F4:8E:92:7F:27:10",	"cyan")
# tuva		= 	Person("Tuva",			"D4:61:2E:F1:E1:7B",	"magenta")
# marit		=	Person("Marit",			"F0:DB:E2:49:29:EE",	"magenta")
# anna		=	Person("Anna",			"BC:6C:21:84:64:A9",	"magenta")
#
# alle = [havard, frederik, raymi, tormod, kabbe, tuva, marit, anna]

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
			print(person.name + " was kicked out.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Kicking everyone out.")
		kick_everyone_out()
		print("Shutting down.")
