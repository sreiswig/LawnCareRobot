import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NMotorDriveController
from Motor import Motor
import time

GPIO.setmode(GPIO.BOARD)

# TO-DO: Make and Read from JSON init file
Channels = [31, 33, 35, 37]
motor1Pins = [35, 37]
motor2Pins = [31, 33]

GPIO.setup(Channels, GPIO.OUT)

motor1 = Motor(motor1Pins)
motor2 = Motor(motor2Pins)

DriveController = L298NMotorDriveController(motor1, motor2)

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