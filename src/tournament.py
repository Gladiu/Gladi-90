import json
import numpy as np
from participant import Participant

class Tournament_SM:
    names = np.array([]) 
    participants = np.array([])
    
    def __init__(self):


        json_file = "../assets/names.json"

        with open(json_file) as json_data:
            buffer_names = json.load(json_data)

        self.names = np.array(buffer_names)
    
    def Register_Player(self):
        pass 
