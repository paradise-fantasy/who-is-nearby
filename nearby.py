#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time

from Person import Person
from handleBluetooth import check_home


havard		=	Person("Håvard",		"40:B8:37:2C:C6:9F", 	"blue")
frederik	=	Person("Frederik",		"F0:24:75:73:CE:7F",	"green")
raymi		=	Person("Raymi",			"84:8E:DF:4B:D7:9F",	"red")
tormod		=	Person("Tormod",		"F4:8E:92:7F:27:12",	"yellow")
kabbe		=	Person("Jon-Anders",	"F4:8E:92:7F:27:10",	"magenta")

alle = [havard, frederik, raymi, tormod, kabbe]


def main():
	print("""Paradise: Who's home?""")
	while True:

		for person in alle:
			check_home(person)

		time.sleep(2)

if __name__ == "__main__":
	main()
