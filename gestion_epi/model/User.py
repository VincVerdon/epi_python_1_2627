'''!
@author: N.Carree
@version: 20261119
'''

class User():
    '''!
    Classe métier représentant les utilisateurs / contrôleurs EPI (users)
    '''
    
    def __init__(self, first_name:str=None, last_name:str=None, login:str=None, password:str=None, id:int=None):
        '''!
        Constructor
        '''
        self.__id = id
        self.__firstName = first_name
        self.__lastName = last_name
        self.__login = login
        self.__password = password
    
    
    def __str__(self) -> str:
        return (
            "id = " + str(self.__id)
            + " ; firstName = " + str(self.__firstName)
            + " ; lastName = " + str(self.__lastName)
            + " ; login = " + str(self.__login)
        )
    
    
    def getId(self):
        return self.__id
    
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getLogin(self):
        return self.__login
    
    def getPassword(self):
        return self.__password
    
    def setId(self, value):
        self.__id = value
        
    def setFirstName(self, value):
        self.__firstName = value
        
    def setLastName(self, value):
        self.__lastName = value
        
    def setLogin(self, value):
        self.__login = value
        
    def setPassword(self, value):
        self.__password = value