import json
from participant import Participant

class Tournament:
    names = []
    participants = []
    seed_required = False
    
    def __init__(self):

        json_file = "assets/names.json"

        with open(json_file) as json_data:
            names = json.load(json_data)
        
        

    def pick_nick(self):
        return_value = 'DEFAULT_NAME'
        return return_value


    async def participant_register(self, user):
        # Check if user has already registered
        if next(filter(lambda arr : arr.id == user.name, self.participants), None) == None: 
            new_participant = Participant()
            new_participant.nick = self.pick_nick()
            new_participant.id = user.name

            if user.dm_channel is None:
               await user.create_dm()
            new_participant.dm_channel = user.dm_channel

            self.participants.append(new_participant)
            seed_required = True

            self.export_data_to_json()
            return True
        else:
            return False
        
    def export_data_to_json(self):
        export_file = open("shared_data/tournament_info.json", "w")
        json_export_array = []
        for participant in self.participants:
            participant_dict = {}
            participant_dict["id"] = participant.id
            participant_dict["nick"] = participant.nick
            participant_dict["seed"] = participant.seed
            participant_dict["opponent_id"] = participant.opponent_id
            json_export_array.append(participant_dict)
        export_file.write(json.dumps(json_export_array))