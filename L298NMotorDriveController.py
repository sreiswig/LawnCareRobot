from Motor import Motor

class L298NMotorDriveController():
    _motorA = Motor()
    _motorB = Motor()

    def __init__(self, motorA, motorB):
        self._motorA = motorA
        self._motorB = motorB

    def MoveForwards(self):
        self._motorA.RotateClockWise()
        self._motorB.RotateCounterClockWise()

    def MoveBackwards(self):
        self._motorA.RotateCounterClockWise()
        self._motorB.RotateClockWise()

    def TurnLeft(self):
        self._motorA.RotateClockWise()
        self._motorB.RotateClockWise()

    def TurnRight(self):
        self._motorA.RotateCounterClockWise()
        self._motorB.RotateCounterClockWise()
    
    def Stop(self):
        self._motorA.Stop()
        self._motorB.Stop()