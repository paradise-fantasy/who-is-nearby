class Person:
	def __init__(self, name, mac, color):
		self.bluetoothPresence = False
		self.name = name
		self.mac = mac
		self.color = color

	def isPresent(self):
		return self.bluetoothPresence
	def setPresence(self, presence):
		self.bluetoothPresence = presence
	def getColor(self):
		return self.color
