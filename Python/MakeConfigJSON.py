import json

# Hardcode the Questions for config for now.
config = []
Motor1 = {}
Motor2 = {}
Pump = {}
Arm = {}
DriveController = {}
PumpAndArmController = {}
MqttCredentials = {}

Motor1["pin1"] = input("Enter Motor1 pin1: ")
Motor1["pin2"] = input("Enter Motor1 pin2: ")
Motor2["pin1"] = input("Enter Motor2 pin1: ")
Motor2["pin2"] = input("Enter Motor2 pin2: ")
Pump["pin1"] = input("Enter Pump pin1: ")
Pump["pin2"] = input("Enter Pump pin2: ")
Arm["pin1"] = input("Enter Arm pin1: ")
Arm["pin2"] = input("Enter Arm pin2: ")
DriveController = {"motor" : [ Motor1 , Motor2 ]}
PumpAndArmController = { "pump" : Pump , "arm" : Arm }
MqttCredentials["clientId"] = input("Enter MQTT clientId: ")
MqttCredentials["host"] = input("Enter Host IP: ")

config = { "driveController" : DriveController, "pumpAndArmController" : PumpAndArmController, "mqtt" : MqttCredentials }

with open('Python/config.json', 'w') as outfile:
    json.dump(config, outfile)