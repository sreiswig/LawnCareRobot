import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import json
import paho.mqtt.client as mqtt

DriveController = {}
ArmController = {}

def on_message(client, userdata, message):
    print("message received " , str(message.payload.decode("utf-8")))
    if(message == "w"):
        DriveController.MoveForwards()
        print("DriveController.MoveForwards Commands was executed")
    
    if(message == "s"):
        DriveController.MoveBackwards()
    
    if(message == "a"):
        DriveController.TurnLeft()
    
    if(message == "d"):
        DriveController.TurnRight()
    
    if(message == " "):
        DriveController.Stop()
    
    if(message == "q"):
        ArmController.RotateArmLeft()
    
    if(message == "e"):
        ArmController.RotateArmRight()
    
    if(message == "stopArm"):
        ArmController.StopArm()

    if(message == "f"):
        ArmController.Spray()

    if(message == "g"):
        ArmController.Reverse()

    if(message == "stopPump"):
        ArmController.StopPump()
    return message

def read_config():
    with open("config.json") as config_file:
        config = json.load(config_file)
    
    return config

# Terminate using command line
def main():
    # Read from some generic config file in json format
    config = read_config()
    if "driveController" in config.keys():
        if "motor" in config["driveController"].keys():
            print("driveController initialized")
            driveMotor1 = Motor([config["driveController"]["motor"][0]["pin1"], config["driveController"]["motor"][0]["pin2"]])
            driveMotor2 = Motor([config["driveController"]["motor"][1]["pin1"], config["driveController"]["motor"][1]["pin2"]])
            DriveController = L298NTrackMotorController(driveMotor1, driveMotor2)

    if "pumpAndArmController" in config.keys():
        if "pump" in config["pumpAndArmController"].keys():
            pump = Motor([config["pumpAndArmController"]["pump"]["pin1"], config["pumpAndArmController"]["pump"]["pin2"]])
            arm = Motor([config["pumpAndArmController"]["arm"]["pin1"], config["pumpAndArmController"]["arm"]["pin2"]])
            ArmController = L298NArmAndPumpController(pump, arm)

    if "mqtt" in config.keys():
        mqttClientId = config["mqtt"]["clientId"]
        mqttHost = config["mqtt"]["host"]
        client = mqtt.Client(mqttClientId)
        client.connect(mqttHost)
        # attach to callback
        client.on_message = on_message
        client.loop_start()
        client.publish("robotCommands", "Robot Initialized")
        client.subscribe("robotCommands")
        
    command = "start"
    while command != "stop":
        command = input("Enter 'stop' to quit: ")

    

if __name__ == '__main__':
    main()