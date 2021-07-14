import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("message received " , str(message.payload.decode("utf-8")))
    command = str(message.payload.decode("utf-8"))
    if(command == "w"):
        DriveController.MoveForwards()
    
    if(command == "s"):
        DriveController.MoveBackwards()
    
    if(command == "a"):
        DriveController.TurnLeft()
    
    if(command == "d"):
        DriveController.TurnRight()
    
    if(command == " "):
        DriveController.Stop()
    
    if(command == "q"):
        ArmController.RotateArmLeft()
    
    if(command == "e"):
        ArmController.RotateArmRight()
    
    if(command == "stopArm"):
        ArmController.StopArm()

    if(command == "f"):
        ArmController.Spray()

    if(command == "g"):
        ArmController.Reverse()

    if(command == "stopPump"):
        ArmController.StopPump()

    if(command == "stop"):
        GPIO.cleanup()
        DriveController.Stop()
        ArmController.Stop()
        client.disconnect()

    return message

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
        motor1Pins = [config["driveController"]["motor"][0]["pin1"], config["driveController"]["motor"][0]["pin2"]]
        motor2Pins = [config["driveController"]["motor"][1]["pin1"], config["driveController"]["motor"][1]["pin2"]]
        driveMotor1 = Motor(motor1Pins)
        driveMotor2 = Motor(motor2Pins)
        DriveController = L298NTrackMotorController(driveMotor1, driveMotor2)
        Channels + motor1Pins
        Channels + motor2Pins

if "pumpAndArmController" in config.keys():
    if "pump" in config["pumpAndArmController"].keys():
        print("Initializing Pump and Arm Controller")
        pumpPins = [config["pumpAndArmController"]["pump"]["pin1"], config["pumpAndArmController"]["pump"]["pin2"]]
        armPins = [config["pumpAndArmController"]["arm"]["pin1"], config["pumpAndArmController"]["arm"]["pin2"]]
        pump = Motor(pumpPins)
        arm = Motor(armPins)
        ArmController = L298NArmAndPumpController(pump, arm)
        Channels + pumpPins
        Channels + armPins

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Channels, GPIO.OUT)

if "mqtt" in config.keys():
    mqttClientId = config["mqtt"]["clientId"]
    mqttHost = config["mqtt"]["host"]
    client = mqtt.Client(mqttClientId)
    client.connect(mqttHost)
    # attach to callback
    client.on_message = on_message
    client.publish("robotCommands", "Robot Initialized")
    client.subscribe("robotCommands")
    client.loop_forever()