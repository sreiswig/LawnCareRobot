import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NMotorDriveController
from Motor import Motor
import time

GPIO.setmode(GPIO.BOARD)

# TO-DO: Read from JSON provided from some db somewhere over the rainbow
Channels = (35, 37)

GPIO.setup(Channels, GPIO.OUT)

motor1 = Motor([35, 37])

motor1.RotateClockwise()
time.sleep(5)

motor1.Stop()
time.sleep(5)

motor1.RotateCounterClockwise()
time.sleep(5)

motor1.Stop()

GPIO.cleanup()