import time
import paho.mqtt.client as mqtt
from dotenv import dotenv_values

config = dotenv_values("pubSubPi.env")

hostname = config["HOSTNAME"]
broker_port = int(config["BROKER_PORT"])
in_topic = config["IN_TOPIC"]
out_topic = config["OUT_TOPIC"]


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    client.subscribe(in_topic)


def on_message(client, userdata, msg):
    print("Message received: " + msg.payload.decode())
    

# Create MQTT client instance
client = mqtt.Client()

# Create and set MQTT callback functions for MQTT connection then subscribe
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker using connect() api and keepalive for 60s
client.connect(hostname, broker_port, 60)

payload = "test message from raspberrypi"
print("Publishing " + payload + " to topic: " + out_topic)
client.publish(out_topic, payload)
client.loop_forever()