import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NMotorDriveController
from Motor import Motor
import time

GPIO.setmode(GPIO.BOARD)

# TO-DO: Make and Read from JSON init file
Channels = [35, 37]

GPIO.setup(Channels, GPIO.OUT)

motor1 = Motor(Channels)

DriveController = L298NMotorDriveController(motor1, motor1)

DriveController.MoveForwards()
time.sleep(5)

DriveController.Stop()
time.sleep(5)

DriveController.MoveBackwards()
time.sleep(5)

DriveController.Stop()
time.sleep(5)

DriveController.TurnLeft()
time.sleep(5)

DriveController.Stop()
time.sleep(5)

DriveController.TurnRight()
time.sleep(5)

GPIO.cleanup()