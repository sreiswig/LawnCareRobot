import Jetson.GPIO as GPIO

class Motor:
    _controlPins = []

    def __init__(self, controlPins=[1, 2]):
        self._controlPins = controlPins

    def Stop(self):
        GPIO.output(self._controlPins, GPIO.LOW)

    def RotateClockwise(self):
        GPIO.output(self._controlPins[0], GPIO.LOW)
        GPIO.output(self._controlPins[1], GPIO.HIGH)

    def RotateCounterClockwise(self):
        GPIO.output(self._controlPins[0], GPIO.HIGH)
        GPIO.output(self._controlPins[1], GPIO.LOW)