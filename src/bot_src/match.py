from enum import Enum

class Match_State(Enum):
    NOT_STARTED = 1
    STARTED = 2
    FINISHED = 3

class Match:
    players = []
    match_state = Match_State.NOT_STARTED
    winner = ''
    stage = 0
    
    def __init__(self) -> None:
        self.players = []
        self.match_state = Match_State.NOT_STARTED
        self.winner = ''
        self.stage = 0
    