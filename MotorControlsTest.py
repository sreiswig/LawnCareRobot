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

print("Moving Forwards")
DriveController.MoveForwards()
time.sleep(5)

print("Stopping")
DriveController.Stop()
time.sleep(5)

print("Moving BackWards")
DriveController.MoveBackwards()
time.sleep(5)

print("Stopping")
DriveController.Stop()
time.sleep(5)

print("Turning Left")
DriveController.TurnLeft()
time.sleep(5)

print("Stopping")
DriveController.Stop()
time.sleep(5)

print("Turning Right")
DriveController.TurnRight()
time.sleep(5)

print("Stopping")
DriveController.Stop()

GPIO.cleanup()