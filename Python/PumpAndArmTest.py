import Jetson.GPIO as GPIO
from L298NMotorDriveController import L298NArmAndPumpController
from Motor import Motor
import time

# Script to test the Motors used 

GPIO.setmode(GPIO.BOARD)

# TO-DO: Make and Read from JSON init file
Channels = [31, 33, 35, 37, 32]
PumpPins = [35, 37]
motor2Pins = [31, 33]

GPIO.setup(Channels, GPIO.OUT)

pump = Motor(PumpPins)
motor2 = Motor(motor2Pins)

SprayController = L298NArmAndPumpController(pump, motor2)
# Setup pin 32 for pwm with frequency 100 Hz
p = GPIO.PWM(32, 100)


GPIO.cleanup()