from model.members import Members


class teams:
    def __init__(self,
                 teamID:int=None,
                 name:str=None,
                 coach:str=None,
                 membersID=None
                 ):
        self.set_teamID(teamID)
 

    def set_Id_teams(self, Id_tams:int):
        self.teamID = Id_tams

    def set_name(self, name:str):
        self.name = name

    def set_coach(self, coach:str):
        self.coach = coach

    def get_Id_teams(self) -> int:
        return self.Id_teams

    def get_name(self) -> str:
        return self.name
    
    def get_coach(self) -> str:
        return self.coach
    
    def to_string(self) -> str:
        return f"teamID: {self.get_teamID} | name: {self.get_name} | coach: {self.get_coach} | membersID: {Members.get_membersID}"
