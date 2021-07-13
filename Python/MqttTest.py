import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("message received " , str(message.payload.decode("utf-8")))
    return message

def read_config():
    with open("config.json") as config_file:
        config = json.load(config_file)
    
    return config

# Terminate using command line
def main():
    # Read from some generic config file in json format
    config = read_config()
    mqttConfig = config["mqtt"]
    client = mqtt.Client("LawnRobot")
    client.connect(mqttConfig["host"])

    client.publish("robotCommands", "Hello From Robot")

if __name__ == '__main__':
    main()