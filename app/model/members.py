class Members:
    def __init__(self,
                 Players:dict=None
                ):
        self.set_Players(Players)

    def set_Players(self, players:any):
        if players != None:
            self.Players.append(players)

    def get_membersID(self) -> int:
        return self.membersID
    
    def get_players(self, nome):
        return self.players
    
    
    def to_string(self) -> str:
        return f" membersID: {self.get_membersID} | Player1: {self.get_Player1} | Player2: {self.get_Player2} | Player3: {self.get_Player3} | Player4: {self.get_Player4} | Player5: {self.get_Player5}"