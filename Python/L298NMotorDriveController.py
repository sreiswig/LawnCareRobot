from Motor import Motor

class L298NTrackMotorController():
    _motorA = Motor()
    _motorB = Motor()

    def __init__(self, motorA, motorB):
        self._motorA = motorA
        self._motorB = motorB

    def MoveBackwards(self):
        self._motorA.RotateClockwise()
        self._motorB.RotateCounterClockwise()

    def MoveForwards(self):
        self._motorA.RotateCounterClockwise()
        self._motorB.RotateClockwise()

    def TurnRight(self):
        self._motorA.RotateClockwise()
        self._motorB.RotateClockwise()

    def TurnLeft(self):
        self._motorA.RotateCounterClockwise()
        self._motorB.RotateCounterClockwise()
    
    def Stop(self):
        self._motorA.Stop()
        self._motorB.Stop()

class L298NArmAndPumpController():
    _pump = []
    _arm = []

    def __init__(self, pump, arm):
        self._pump = pump
        self._arm = arm

    def RotateArmLeft(self):
        self._arm.RotateCounterClockwise()

    def RotateArmRight(self):
        self._arm.RotateClockwise()
    
    def StopArm(self):
        self._arm.Stop()

    def Spray(self):
        # TO-DO: Pump Control
        self._pump.RotateClockwise()

    def Reverse(self):
        self._pump.RotateCounterClockwise()

    def StopPump(self):
        self._pump.Stop()

    def Stop(self):
        self._pump.Stop()
        self._arm.Stop()
    