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

    def Pick_Nick(self):
        return_value = 'DEFAULT_NAME'
        return return_value


    async def Participant_Register(self, user):
        # Check if user has already registered
        if next(filter(lambda arr : arr.id == user.name, self.participants), None) == None: 
            new_participant = Participant()
            new_participant.nick = self.Pick_Nick()
            new_participant.id = user.name
            if user.dm_channel is None:
               await user.create_dm()
            new_participant.dm_channel = user.dm_channel
            await user.dm_channel.send("ASDDAS")
            self.participants.append(new_participant)
            seed_required = True

            return True
        else:
            return False
        