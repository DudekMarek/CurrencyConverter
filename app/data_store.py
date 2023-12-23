import json
import os
from currency import Currency

class DataHandler():

    def __init__(self, json_name: str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_path: str = os.path.join(current_dir, "data" ,json_name)
        self.data: dict = dict()
    
    
    def read_data(self):
        
        with open(self.json_path, 'r') as file:
            data = json.load(file)
        
        self.data = data
    
    def write_data(self):
        directory = os.path.dirname(self.json_path)
        
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(self.json_path, "w") as file:
            json.dump(self.data, file, indent=None, separators=(',', ':'))

    def list_stored_currencies(self):
        return [item for item in self.data]
    
    def add_currency(self, currency: Currency):
        self.data.update(currency.return_dict())
        self.write_data()