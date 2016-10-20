import paho.mqtt.publish as publish

data_topic = "paradise/log/presence"
notify_topic = "paradise/notify/presence"
everyone_present_topic = "paradise/flamingo/notify"

ca = "ca.crt"

def send_presence_event(presence_event):
	data = str(presence_event)

	publish.single(data_topic, data, port=1883, hostname="nyx.bjornhaug.net")
	publish.single(notify_topic, data, port=1883, hostname="nyx.bjornhaug.net")

def send_everyone_present():
	data = "true"
	publish.single(everyone_present_topic, data, port=1883, hostname="nyx.bjornhaug.net")
