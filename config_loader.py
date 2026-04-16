import os
import json

def loadconfig(config_path= "config.json"):
    #check if config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f'File not found at {config_path}')
    #open and read the config file
    with open(config_path, 'r') as config_file: 
        config = json.load(config_file)
    return config

