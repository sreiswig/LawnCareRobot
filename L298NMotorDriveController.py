from Motor import Motor

class L298NMotorDriveController():
    _motorA = Motor()
    _motorB = Motor()

    def __init__(self, motorA, motorB):
        self._motorA = motorA
        self._motorB = motorB

    def MoveForwards(self):
        self._motorA.RotateClockwise()
        self._motorB.RotateCounterClockwise()

    def MoveBackwards(self):
        self._motorA.RotateCounterClockwise()
        self._motorB.RotateClockwise()

    def TurnLeft(self):
        self._motorA.RotateClockwise()
        self._motorB.RotateClockwise()

    def TurnRight(self):
        self._motorA.RotateCounterClockwise()
        self._motorB.RotateCounterClockwise()
    
    def Stop(self):
        self._motorA.Stop()
        self._motorB.Stop()