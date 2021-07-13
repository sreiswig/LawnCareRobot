import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import time

# Script to test the Motors used 

GPIO.setmode(GPIO.BOARD)

# TO-DO: Make and Read from JSON init file
Channels = [19, 21, 23, 29, 31, 33, 35, 37]
motor1Pins = [35, 37]
motor2Pins = [31, 33]
armPins = [23, 29]
pumpPins = [19, 21]

GPIO.setup(Channels, GPIO.OUT)

motor1 = Motor(motor1Pins)
motor2 = Motor(motor2Pins)
arm = Motor(armPins)
pump = Motor(pumpPins)

DriveController = L298NTrackMotorController(motor1, motor2)
ArmController = L298NArmAndPumpController(pump, arm)

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

    if(command == "stopPump"):
        ArmController.StopPump()
        continue

DriveController.Stop()
GPIO.cleanup()