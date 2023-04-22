from teams import teamID
from matches import matchID

class groups:
    def __init__(self,
                 groupID:int=None,
                 nameGroup:str=None,
                 teamID1:teamID=None,
                 teamID2:teamID=None,
                 teamID3:teamID=None,
                 teamID4:teamID=None,
                 matchID1:matchID=None,
                 matchID2:matchID=None,
                 matchID3:matchID=None,
                 winner:teamID=None
                 ):
        self.set_groupID(groupID)
        self.set_nameGroup(nameGroup)
        self.set_teamID1(teamID1)
        self.set_teamID2(teamID2)
        self.set_teamID3(teamID3)
        self.set_teamID4(teamID4)
        self.set_matchID1(matchID1)
        self.set_matchID2(matchID2)
        self.set_matchID3(matchID3)
        self.set_winner(winner)

    def set_groupID(self, groupID:int):
        self.groupID = groupID

    def set_nameGroup(self, nameGroup:str):
        self.nameGroup = nameGroup
    
    def set_teamID1(self, teamID1:teamID):
        self.teamID1 = teamID1
        
    def set_teamID2(self, teamID2:teamID):
        self.teamID2 = teamID2

    def set_teamID3(self, teamID3:teamID):
        self.teamID3 = teamID3

    def set_teamID4(self, teamID4:teamID):
        self.teamID4 = teamID4

    def set_matchID1(self, matchID1:matchID):
        self.mathcID1 = matchID1

    def set_matchID2(self, matchID2:matchID):
        self.mathcID2 = matchID2

    def set_matchID3(self, matchID3:matchID):
        self.mathcID3 = matchID3

    def set_winner(self, winner:matchID):
        self.winner = winner

    def get_groupID(self) -> int:
        return self.groupID
    
    def get_nameGroup(self) -> str:
        return self.nameGroup
    
    def get_teamID1(self) -> teamID:
        return self.teamID1
    
    def get_teamID2(self) -> teamID:
        return self.teamID2
    
    def get_teamID3(self) -> teamID:
        return self.teamID3
    
    def get_teamID4(self) -> teamID:
        return self.teamID4
    
    def get_matchID1(self) -> matchID:
        return self.mathcID1
    
    def get_matchID2(self) -> matchID:
        return self.mathcID2
    
    def get_matchID3(self) -> matchID:
        return self.mathcID3
    
    def get_winner(self) -> teamID:
        return self.winner
    
    def to_string(self) -> str:
        return f"groupID: {self.get_groupID} | nameGroup: {self.get_nameGroup} | teamID1: {self.get_teamID1} | teamID2: {self.get_teamID2} | teamID3: {self.get_teamID3} | teamID4: {self.get_teamID4} | matchID1: {self.mathcID1} | matchID2: {self.mathcID2} | matchID3: {self.mathcID3} | winner: {self.get_winner}"