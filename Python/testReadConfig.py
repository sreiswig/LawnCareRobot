import json

def read_config():
    with open("Python/config.json") as config_file:
        config = json.load(config_file)
    
    return config

config = read_config()

print(config["driveController"])
print(config["pumpAndArmController"])
print(config["mqtt"])