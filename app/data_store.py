import json
import os

class DataHandler():

    def __init__(self, json_name: str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_path: str = os.path.join(current_dir, "data" ,json_name)
        self.data: dict = None
    
    
    def read_data(self):
        
        with open(self.json_path, 'r') as file:
            data = json.load(file)
        
        self.data = data
    
    def write_data(self, data):
        directory = os.path.dirname(self.json_path)
        
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(self.json_path, "w") as file:
            json.dump(data, file, indent=None, separators=(',', ':'))

    def list_stored_currencies(self):
        return [item for item in self.data]