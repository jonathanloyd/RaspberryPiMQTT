import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected to MQTT broker with result code: " + str(rc))
	client.subscribe(topic)

def on_message(client, userdata, msg):
	print("Message received: " + msg.payload.decode())

hostname = "raspberrymqtthost"
broker_port = 1883
topic = "test/topic"

# Create MQTT client instance
client = mqtt.Client()

# Create and set MQTT callback functions for MQTT connection then subscribe
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker using connect() api and keepalive for 60s
client.connect(hostname, broker_port, 60)

payload = "test message from raspberrypi"
print("Publishing " + payload + " to topic: " + topic)
client.publish(topic, payload)
