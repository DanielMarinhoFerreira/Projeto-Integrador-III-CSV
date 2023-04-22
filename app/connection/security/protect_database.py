from dotenv import dotenv_values
import os



class Protect:
        
    def __init__(self, conect:bool=True):
        self.__connect = conect
           
    def key_database(self, key=str):
        self.config_ = os.path.expanduser('~\\OneDrive\\Faculdade\\Projeto Integrador III\\app\\connection\\security\\db.env')
        info = dotenv_values(self.config_, encoding="utf-8")  
        
        
        if info != None and self.__connect:
            return info[key]
        else :
            return 
        
    def query_sql(self, file_query:str) ->str:
        '''
        Função que busca a query no arquivo informado.
        @self.config_ : local aonda se enconrar os arquivos slq
        return query -> que tem nesse aquivo.
        '''
        self.config_ = os.path.expanduser('~\\OneDrive\\Faculdade\\Projeto Integrador III\\sql\\')
        caminho = self.config_+file_query+'.sql'
        with open(caminho) as query_read:
            query = query_read.read()
            
            if query != None:
                return query
            else:
                return