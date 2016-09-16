#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person:
	def __init__(self, ID, name, bluetooth_address, color, room):
		self.ID = ID
		self.bluetoothPresence = False
		self.name = name
		self.bluetooth_address = bluetooth_address
		self.color = color
		self.room = room

	def isPresent(self):
		return self.bluetoothPresence
	def setPresence(self, presence):
		self.bluetoothPresence = presence
	def getColor(self):
		return self.color
