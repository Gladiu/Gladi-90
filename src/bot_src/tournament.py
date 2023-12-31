import json
from random import randrange
from participant import Participant
from match import Match

class Tournament:
    names = []
    participants = []
    matches = []
    
    def import_names(self):
        json_file = "src/assets/names.json"
        with open(json_file) as json_data:
            self.names = json.load(json_data)
        

    def pick_nick(self, id):
        # Randomly pick names untill its not taken
        # TODO: detect if all names are taken
        return_nick = self.names[randrange(len(self.names))]
        while next(filter(lambda arr : arr.nick == return_nick, self.participants), None) != None: 
            return_nick = self.names[randrange(len(self.names))]
            print(return_nick )
        return return_nick


    async def participant_register(self, user):
        # Check if user has already registered
        if next(filter(lambda arr : arr.id == user.name, self.participants), None) == None: 
            new_participant = Participant()
            new_participant.id = user.name
            new_participant.nick = self.pick_nick(new_participant.id)


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
        export_file = open("src/shared_data/tournament_info.json", "w")
        json_export_array = []
        for participant in self.participants:
            participant_dict = {}
            participant_dict["id"] = participant.id
            participant_dict["nick"] = participant.nick
            participant_dict["opponent_id"] = participant.opponent_id
            json_export_array.append(participant_dict)
        export_file.write(json.dumps(json_export_array))

    def update_seeds_from_json(self):
        json_file = "src/shared_data/seeded_players.json"
        with open(json_file) as json_data:
            seeded_players = json.load(json_data)
            for participant in self.participants:
                participant.seed = seeded_players[participant.id]
            self.export_data_to_json()

    def generate_matches(self):

        self.participants.sort(key=lambda x: (x.seed))

        # Stage 0 matches
        # Stage with most matches

        stage_0_players = 2
        while stage_0_players * 2 <= len(self.participants):         
            stage_0_players = stage_0_players * 2


        for i in range(0, int(stage_0_players/2)):

                new_match = Match()
                
                # Higher seeded player always goes first
                new_match.players.append(self.participants[i])
                new_match.players.append(self.participants[stage_0_players - 1 - i])

                self.matches.append(new_match)


        surplus_stage_0_players = len(self.participants) - stage_0_players


        if surplus_stage_0_players > 0:

            stage_minus_1_players = 0
            stage_minus_2_players = 0
            
            if surplus_stage_0_players > stage_0_players * 0.5:
                # stage_0_players is always power of 2
                stage_minus_1_players = int(stage_0_players * 0.75) - 1
                stage_minus_2_players = surplus_stage_0_players - stage_minus_1_players
            else:
                stage_minus_1_players = surplus_stage_0_players


            # Stage -1

            for i in range(0, stage_minus_1_players):
                new_match = Match()
                new_match.stage = -1

                # Higher seeded player always goes first
                new_match.players.append(self.matches[i].players[1])
                new_match.players.append(self.participants[i+stage_0_players])

                self.matches[i].players[1] = Participant()
                self.matches[i].players[1].nick = 'Winner of Match %d' % int(len(self.matches))

                self.matches.append(new_match)

            # Stage -2
            for i in range(0, stage_minus_2_players):
                new_match = Match()
                new_match.stage = -2

                # Each player in stage -1 got its match
                new_match.players.append(self.matches[i+int(stage_0_players/2)].players[1])
                new_match.players.append(self.participants[i+stage_0_players+stage_minus_1_players])

                self.matches[i+int(stage_0_players/2)].players[1] = Participant()
                self.matches[i+int(stage_0_players/2)].players[1].nick = 'Winner of Match %d' % int(len(self.matches))

                self.matches.append(new_match)


        # Stage 0< matches
        # Further matches up to grand finals