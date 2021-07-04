import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NTrackMotorController
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import time

# Script to test the Motors used 

GPIO.setmode(GPIO.BOARD)

# TO-DO: Make and Read from JSON init file
Channels = [31, 33, 35, 37]
motor1Pins = [35, 37]
motor2Pins = [31, 33]

GPIO.setup(Channels, GPIO.OUT)

motor1 = Motor(motor1Pins)
motor2 = Motor(motor2Pins)

DriveController = L298NTrackMotorController(motor1, motor2)

command = "start"
while command != "stop":
    command = raw_input("Enter Command: ")

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

GPIO.cleanup()