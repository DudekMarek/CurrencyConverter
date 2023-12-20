import json
import os

class DataHandler():

    def __init__(self, json_name: str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_path = os.path.join(current_dir, json_name)
        self.data = None
    
    def read_data(self):
        
        with open(self.json_path, 'r') as file:
            data = json.load(file)
        
        self.data = data
    
    def write_data(self, data):

        with open(self.json_path, "w") as file:
            json.dump(data, file, indent=None, separators=(',', ':'))
        