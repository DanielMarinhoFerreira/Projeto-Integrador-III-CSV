from groupStage import groupStageID
from playoffs import playoffsID
from teams import teamsID

class tournaments:
    def __init__(self,
                 tournamentsID:int=None,
                 tournamentsName:str=None,
                 groupStageID:groupStageID=None,
                 playoffsID:playoffsID=None,
                 prizePool:float=None,
                 winner:teamsID=None,
                 ):
        self.set_tounamentsID(tournamentsID)
        self.set_tournamentsName(tournamentsName)
        self.set_groupStageID(groupStageID)
        self.set_playoffsID(playoffsID)
        self.set_prizePool(prizePool)
        self.set_winner(winner)

    def set_tournametsID(self, tournamentsID:int):
        self.tournamentsID = tournamentsID

    def set_tournamentsName(self, tournamentsName:str):
        self.set_tournamentsName = tournamentsName

    def set_groupStageID(self, groupStageID:groupStageID):
        self.groupStageID = groupStageID

    def set_playoffsID(self, playoffsID:playoffsID):
        self.playoffsID = playoffsID

    def set_prizePool(self, prizePool:float):
        self.prizePool = prizePool

    def set_winner(self, winner:teamsID):
        self.winner = winner

    def get_tournamentsID(self) -> int:
        return self.tournamentsID
    
    def get_tournamentsName(self) -> str:
        return self.tournamentsName
    
    def get_groupStageID(self) -> groupStageID:
        return self.groupStageID
    
    def get_playoffsID(self) -> playoffsID:
        return self.playoffsID
    
    def get_prizePool(self) -> float:
        return self.prizePool
    
    def get_winner(self) -> teamsID:
        return self.winner
    
    def to_string(self) -> str:
        return f"tournamentsID: {self.get_tournamentsID} | tournamentsName: {self.get_tournamentsName} | groupStageID: {self.get_groupStageID} | playoffsID: {self.get_playoffsID} | prizePool: {self.get_prizePool} | winner: {self.get_winner}"
