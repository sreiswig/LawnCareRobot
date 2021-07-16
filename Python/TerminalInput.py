import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import time
import json

def read_config():
    with open("config.json") as config_file:
        config = json.load(config_file)
    
    return config

# Read from some generic config file in json format
Channels = []
config = read_config()
if "driveController" in config.keys():
    if "motor" in config["driveController"].keys():
        print("Initializing Drive Controller")
        motor1Pins = [int(config["driveController"]["motor"][0]["pin1"]), int(config["driveController"]["motor"][0]["pin2"])]
        motor2Pins = [int(config["driveController"]["motor"][1]["pin1"]), int(config["driveController"]["motor"][1]["pin2"])]
        driveMotor1 = Motor(motor1Pins)
        driveMotor2 = Motor(motor2Pins)
        DriveController = L298NTrackMotorController(driveMotor1, driveMotor2)
        Channels = Channels + motor1Pins
        Channels = Channels + motor2Pins

if "pumpAndArmController" in config.keys():
    if "pump" in config["pumpAndArmController"].keys():
        print("Initializing Pump and Arm Controller")
        pumpPins = [int(config["pumpAndArmController"]["pump"]["pin1"]), int(config["pumpAndArmController"]["pump"]["pin2"])]
        armPins = [int(config["pumpAndArmController"]["arm"]["pin1"]), int(config["pumpAndArmController"]["arm"]["pin2"])]
        pump = Motor(pumpPins)
        arm = Motor(armPins)
        ArmController = L298NArmAndPumpController(pump, arm)
        Channels = Channels + pumpPins
        Channels = Channels + armPins

GPIO.setmode(GPIO.BOARD)
print(Channels)
GPIO.setup(Channels, GPIO.OUT)

command = "start"
while command != "stop":
    command = input("Enter Command: ")
    if(command == "w"):
        DriveController.MoveForwards()
        continue
    
    if(command == "s"):
        DriveController.MoveBackwards()
        continue
    
    if(command == "a"):
        DriveController.TurnLeft()
        continue
    
    if(command == "d"):
        DriveController.TurnRight()
        continue
    
    if(command == " "):
        DriveController.Stop()
        continue
    
    if(command == "q"):
        ArmController.RotateArmLeft()
        continue
    
    if(command == "e"):
        ArmController.RotateArmRight()
        continue
    
    if(command == "stopArm"):
        ArmController.StopArm()
        continue

    if(command == "f"):
        ArmController.Spray()
        continue

    if(command == "g"):
        ArmController.Reverse()
        continue

    if(command == "stopPump"):
        ArmController.StopPump()
        continue

DriveController.Stop()
GPIO.cleanup()