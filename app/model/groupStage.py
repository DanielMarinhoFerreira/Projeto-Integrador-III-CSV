from groups import groupID

class groupStage:
    def __init__(self,
                 groupStageID:int=None,
                 groupID1:groupID=None,
                 groupID2:groupID=None,
                 groupID3:groupID=None,
                 groupID4:groupID=None,
                 ):
        self.set_groupStageID(groupStageID)
        self.set_groupID1(groupID1)
        self.set_groupID2(groupID2)
        self.set_groupID3(groupID3)
        self.set_groupID4(groupID4)

    def set_groupStageID(self, groupStageID:int):
        self.groupStageID = groupStageID

    def set_groupID1(self, groupID1:groupID):
        self.groupID1 = groupID1
    
    def set_groupID2(self, groupID2:groupID):
        self.groupID2 = groupID2

    def set_groupID3(self, groupID3:groupID):
        self.groupID3 = groupID3

    def set_groupID4(self, groupID4:groupID):
        self.groupID4 = groupID4

    def get_groupStageID(self) -> int:
        return self.groupStageID
    
    def get_groupID1(self) -> groupID:
        return self.groupID1
    
    def get_groupID2(self) -> groupID:
        return self.groupID2
    
    def get_groupID3(self) -> groupID:
        return self.groupID3
    
    def get_groupID4(self) -> groupID:
        return self.groupID4
    
    def to_string(self) -> str:
        return f"groupStageID: {self.get_groupStageID} | groupID1: {self.get_groupID1} | groupID2: {self.get_groupID2} | groupID3: {self.get_groupID3} | groupID4: {self.get_groupID4}"