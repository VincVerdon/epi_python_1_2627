'''!
@author: N.Carree
@version: 20261119
'''

from PyQt5.QtWidgets import (
    QMainWindow, QToolBar, QTableWidget, QTableWidgetItem,
    QAbstractItemView, QHeaderView
)
from PyQt5.Qt import QIcon, Qt
from model.User import User


class UserView(QMainWindow):
    '''!
    Vue principale affichant la liste des utilisateurs et permettant ajout, modification et suppression
    '''
    
    def __init__(self, ctrl, usersList: list):
        '''!
        Constructor
        '''
        super().__init__()
        self.__ctrl = ctrl
        
        # Paramétrage et taille de la fenêtre
        self.setWindowTitle("Gestion des utilisateurs (contrôleurs)")
        self.resize(650, 400)
        self.setWindowIcon(QIcon("icons/epi.png"))
        
        # Toolbar avec texte affiché à côté des icônes
        self.__bar = QToolBar("Barre d'outils")
        self.__bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(self.__bar)
        
        self.__actionNew = self.__bar.addAction(QIcon("icons/new.png"), "Ajouter")
        self.__actionMod = self.__bar.addAction(QIcon("icons/edit.png"), "Modifier")
        self.__actionDel = self.__bar.addAction(QIcon("icons/delete.png"), "Supprimer")
        
        # Événements
        self.__actionNew.triggered.connect(self.__ctrl.createUserUI)
        self.__actionMod.triggered.connect(self.__ctrl.updateUserUI)
        self.__actionDel.triggered.connect(self.__ctrl.deleteUserUI)
        
        # Tableau central modernisé
        self.__grid = QTableWidget(self)
        self.setCentralWidget(self.__grid)
        self.__grid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.__grid.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.__grid.setAlternatingRowColors(True)

        self.__grid.setColumnCount(4)
        self.__grid.setHorizontalHeaderLabels(["Numéro", "Prénom", "Nom", "Login"])
        self.__grid.verticalHeader().setVisible(False)
        
        # Étire les colonnes sur toute la largeur de la fenêtre
        header = self.__grid.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        
        self.displayList(usersList)
        self.show()
        
        
    def addRow(self, user: User):
        '''!
        Ajout d'une ligne dans la liste des utilisateurs à afficher
        '''
        row = self.__grid.rowCount()
        self.__grid.setRowCount(row + 1)
        
        itemId = QTableWidgetItem(str(user.getId()))
        itemId.setTextAlignment(Qt.AlignCenter)
        
        self.__grid.setItem(row, 0, itemId)
        self.__grid.setItem(row, 1, QTableWidgetItem(user.getFirstName()))
        self.__grid.setItem(row, 2, QTableWidgetItem(user.getLastName()))
        self.__grid.setItem(row, 3, QTableWidgetItem(user.getLogin()))
        
        
    def displayList(self, usersList: list):
        '''!
        Affiche la liste des utilisateurs à l'écran
        '''
        self.__grid.setRowCount(0)
        for user in usersList:
            self.addRow(user)