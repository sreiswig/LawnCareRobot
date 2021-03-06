import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import json

def read_config():
    with open("config.json") as config_file:
        config = json.load(config_file)
    
    return config

config = read_config()

print(config["driveController"])
print(config["pumpAndArmController"])
print(config["mqtt"])

if "driveController" in config.keys():
    if "motor" in config["driveController"].keys():
        driveMotor1 = Motor([config["driveController"]["motor"][0]["pin1"], config["driveController"]["motor"][0]["pin2"]])
        driveMotor2 = Motor([config["driveController"]["motor"][1]["pin1"], config["driveController"]["motor"][1]["pin2"]])
        driveController = L298NTrackMotorController(driveMotor1, driveMotor2)

if "pumpAndArmController" in config.keys():
    if "pump" in config["pumpAndArmController"].keys():
        pump = Motor([config["pumpAndArmController"]["pump"]["pin1"], config["pumpAndArmController"]["pump"]["pin2"]])
        arm = Motor([config["pumpAndArmController"]["arm"]["pin1"], config["pumpAndArmController"]["arm"]["pin2"]])
        pumpAndArmController = L298NArmAndPumpController(pump, arm)

if "mqtt" in config.keys():
    mqttClientId = config["mqtt"]["clientId"]
    mqttHost = config["mqtt"]["host"]

