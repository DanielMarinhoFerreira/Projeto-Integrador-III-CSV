from connection.security.protect_database import Protect
from api.liquipediapy.liquipediapy import liquipedia
from api.liquipediapy import counterstrike
from bs4 import BeautifulSoup
import time

class LiquiApi:

    def __init__(self):
        """
        Contrutor da class
        """
        self.app_nome = 'Analyst'
        
    def timer(self, seg=30):
        if seg != 0:
                while seg:
                    time.sleep(0.03)
                    seg = seg - 1
        else:
            return False
        return True
        
    def get_cs_page(self, page=str, table=str, debug_database:bool=False):
        """
        Função que realizar bunca pela API(liquipediapy).
        
        """
        if (self.timer()):
            liquipy_object = liquipedia(self.app_nome,'counterstrike', table , debug_database) 
            
            if liquipy_object != None:
                Obj:BeautifulSoup = liquipy_object.parse(page)
                
                return Obj
            else:
                return
        
    def get_cs_player(self, page=str, table=str , debug_database=bool):
        
        if (self.timer()):
            object_cs = counterstrike(self.app_nome, table , debug_database)
            teams = object_cs.get_teams('Western_Europe')
            
        return teams
    