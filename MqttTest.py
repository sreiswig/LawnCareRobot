import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("message received " , str(message.payload.decode("utf-8")))
    return message

# Terminate using command line
def main():
    
    # Read from some generic config file in json format
    settings = json.loads("config.ini")

    host = settings["host"]
    client = mqtt.Client("LawnRobot")
    client.connect(host)

    command = "start"
    while command != "stop":
        command = input("Enter Command: ")

if __name__ == '__main__':
    main()