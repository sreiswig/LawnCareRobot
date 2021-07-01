import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# TO-DO: Read from JSON provided from some db somewhere over the rainbow

Channels = (35, 37)

GPIO.setup(Channels, GPIO.OUT)

GPIO.output(35, GPIO.HIGH)
time.sleep(5)

GPIO.output(35, GPIO.LOW)
time.sleep(1)

GPIO.output(37, GPIO.HIGH)
time.sleep(5)

GPIO.output(37, GPIO.LOW)

GPIO.cleanup()