'''!
@author: N.Carree
@version: 20261119
'''

import json
from api.Api import Api
from model.User import User


class UserApi(Api):
    '''!
    Classe donnant accès à l'API REST distante
    pour la gestion des users
    '''

    def __init__(self):
        '''!
        Constructeur
        @note: appel du constructeur parent obligatoire !
        '''
        super().__init__()
        
    
    def readAll(self):
        '''!
        Récupère la liste des users
        @return: liste d'objets User
        '''
        res = self._get('users')
        if res is None:
            return []
        listUsers = []
        for u in res:
            listUsers.append(
                User(
                    u["first_name"],
                    u["last_name"],
                    u["login"],
                    u.get("password", ""),
                    u["id"]
                )
            )
        return listUsers
    
    
    def create(self, user:User):
        '''!
        Enregistre un nouveau user
        '''
        data = json.dumps({
            "first_name": user.getFirstName(),
            "last_name": user.getLastName(),
            "login": user.getLogin(),
            "password": user.getPassword()
        })
        self._post('users', data)
    
    
    def update(self, user:User):
        '''!
        Mise à jour d'un user
        '''
        data = json.dumps({
            "first_name": user.getFirstName(),
            "last_name": user.getLastName(),
            "login": user.getLogin(),
            "password": user.getPassword()
        })
        self._put('users', data, user.getId())
    
    
    def delete(self, id:int):
        '''!
        Suppression d'un user
        '''
        self._del('users', id)