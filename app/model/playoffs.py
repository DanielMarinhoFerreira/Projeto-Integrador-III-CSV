from matches import matchID

class playoffs:
    def __init__(self,
                 playoffsID:int=None,
                 phase:str=None,
                 matchID:matchID=None
                 ):
        self.set_playoffsID(playoffsID)
        self.set_phase(phase)
        self.set_matchID(matchID)

    def set_playoffsID(self, playoffsID:int):
        self.playoffsID = playoffsID

    def set_phase(self, phase:str):
        self.phase = phase

    def set_matchID(self, matchID:matchID):
        self.matchID = matchID

    def get_playoffsID(self) -> int:
        return self.playoffsID
    
    def get_phase(self) -> str:
        return self.phase
    
    def get_matchID(self) -> matchID:
        return self.matchID
    
    def to_string(self) -> str:
        return f"playoffsID: {self.get_playoffsID} | phase: {self.get_phase} | matchID: {self.get_matchID}"