'''!
@author: N.Carree
@version: 20261119
'''

from api.UserApi import UserApi
from view.UserEditView import UserEditView
from PyQt5.Qt import QInputDialog


class UserCtrl():
    '''!
    Contrôleur pour les vues user
    '''

    def __init__(self):
        '''!
        Constructeur du contrôleur
        '''
        self.__view = None


    def setView(self, view):
        '''!
        Enregistre la vue principale associée au contrôleur
        @param view Instance de UserView
        '''
        self.__view = view


    def __refreshView(self):
        '''!
        Rafraîchit l'affichage du tableau des utilisateurs
        '''
        if self.__view is not None:
            self.__view.displayList(self.getUsersList())

        
    def getUsersList(self):
        '''!
        Récupère la liste des users
        '''
        api = UserApi()
        list_users = api.readAll()
        return list_users
    
    
    def createUserUI(self):
        '''!
        Affichage fenêtre de création d'un nouveau user
        '''
        self.__userForm = UserEditView(self)
       
       
    def createUserProcess(self):
        '''!
        Traitement des données de la fenêtre de création d'un user
        '''
        user = self.__userForm.getUser()
        api = UserApi()
        api.create(user)
        self.__userForm.destroy()
        self.__refreshView()
    
    
    def updateUserUI(self):
        '''!
        Affichage fenêtre d'update d'un user
        '''
        self.__userForm = UserEditView(self, True)
    
    
    def updateUserProcess(self):
        '''!
        Traitement des données de la fenêtre d'update d'un user
        '''
        user = self.__userForm.getUser()
        api = UserApi()
        api.update(user)
        self.__userForm.destroy()
        self.__refreshView()
    
        
    def destroyUserEditUI(self):
        '''!
        Suppression fenêtre d'édition d'un user
        @see updateUserUI
        @see createUserUI
        '''
        self.__userForm.destroy()
    
    def deleteUserUI(self):
        '''!
        Affichage fenêtre de suppression d'un user
        @todo A déplacer dans une vue...
        '''
        self.__userNum = 0
        res = QInputDialog.getInt(
            None,
            "Supprimer un utilisateur",
            "Veuillez saisir le numéro de l'utilisateur à supprimer",
            0,
            self.__userNum
        )
        
        if res[1]:
            self.__userNum = res[0]
            api = UserApi()
            api.delete(res[0])
            self.__refreshView()