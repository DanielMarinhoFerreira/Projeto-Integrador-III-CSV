from model.teams import teamID
from model.tournaments import tournamentsID

class matches:
    def __init__(self,
                 matchID:int=None,
                 teamID1:teamID=None,
                 teamID2:teamID=None,
                 age:int=None,
                 tournamentsID:tournamentsID=None,
                 winner:teamID=None
                 ):
        self.set_matchID(matchID)
        self.set_teamID1(teamID1)
        self.set_teamID2(teamID2)
        self.set_age(age)
        self.set_tournamentsID(tournamentsID)
        self.set_winner(winner)

    def set_matchID(self, matchID:int):
        self.matchID = matchID

    def set_teamID1(self, teamID1:teamID):
        self.teamID1 = teamID1

    def set_teamID2(self, teamID2:teamID):
        self.teamID2 = teamID2

    def set_age(self, age:int):
        self.age = age

    def set_tournamentsID(self, tournamentsID:tournamentsID):
        self.tournamentsID = tournamentsID

    def set_winner(self, winner:teamID):
        self.winner = winner

    def get_matchID(self) -> int:
        return self.matchID
    
    def get_teamID1(self) -> teamID:
        return self.teamID1
    
    def get_teamID2(self) -> teamID:
        return self.teamID2
    
    def get_age(self) -> int:
        return self.age
    
    def get_tournamentsID(self) -> tournamentsID:
        return self.tournamentsID
    
    def get_winner(self) -> teamID:
        return self.winner
    
    def to_string(self) -> str:
        return f"matchID: {self.get_matchID} | teamID1: {self.get_teamID1} | teamID2: {self.get_teamID2} | age: {self.get_age} | tournamentsID: {self.get_tournamentsID} | winner: {self.get_winner}"