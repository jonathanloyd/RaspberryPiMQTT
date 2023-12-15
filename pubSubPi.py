import datetime
import json
import pyodbc
import paho.mqtt.client as mqtt
from dotenv import dotenv_values

config = dotenv_values("pubSubPi.env")

hostname = config["HOSTNAME"]
broker_port = int(config["BROKER_PORT"])
in_topic = config["IN_TOPIC"]
out_topic = config["OUT_TOPIC"]

# Make sure to give the pi's ip firewall permissions in Azure DB Server
db_server = config["DB_SERVER"]
db_name = config["DB_NAME"]
db_username = config["DB_USERNAME"]
db_password = config["DB_PASSWORD"]


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    client.subscribe(in_topic)


def on_message(client, userdata, msg):
    print("Message received: " + msg.payload.decode())
    data = None
    sensorTime, sensorReading = None, None

    try:
        data = json.loads(msg.payload.decode())
    except json.decoder.JSONDecodeError:
        pass  # don't read non-json data
    if data and data["messageType"] == "sensorReading":
        sensorTime = data["epochTime"]
        sensorReading = data["sensorReading"]
        print("Sensor Time: " + str(datetime.datetime.fromtimestamp(sensorTime).strftime('%c')))
        print("Sensor Reading: " + str(sensorReading))

        with dbConnection.cursor() as cursor:
            readingInsertionStatment = "INSERT INTO [dbo].[WifiSensorReadings] (ReadingTime, SensorReading) values (?, ?);"
            cursor.execute(readingInsertionStatment, (str(datetime.datetime.fromtimestamp(sensorTime).strftime('%Y-%m-%d %H:%M:%S')), sensorReading))

# Create DB connection
dbConnectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_username};PWD={db_password}'
dbConnection = pyodbc.connect(dbConnectionString)
print("Connected to DB")

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