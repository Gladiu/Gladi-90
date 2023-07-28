class Participant:
    name = ''
    id = ''
    dm_channel = None
    seed = 0

    def Create(self, name, id):
        self.name = name
        self.id = id

    def Seed(self, seed):
        self.seed = seed
