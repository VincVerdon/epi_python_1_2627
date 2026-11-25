'''!
@author: N.Carree
@version: 20261119
'''

from PyQt5.QtWidgets import (
    QPushButton, QGridLayout, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QLineEdit
)
from PyQt5.Qt import QIcon, Qt
from model.User import User


class UserEditView(QWidget):
    '''!
    Vue permettant la création ou la modification d'un utilisateur
    '''
    
    def __init__(self, ctrl, update: bool = False):
        '''!
        Constructor
        '''
        super().__init__()
        self.__ctrl = ctrl
        
        # Paramétrage et taille du formulaire
        self.setWindowTitle("Modifier un utilisateur" if update else "Ajouter un utilisateur")
        self.resize(380, 240)
        self.setWindowIcon(QIcon("icons/epi.png"))
        
        # Marges et espacements propres
        self.__centralLay = QVBoxLayout()
        self.__centralLay.setContentsMargins(20, 20, 20, 20)
        self.__centralLay.setSpacing(15)
        self.setLayout(self.__centralLay)
        
        self.__gridLay = QGridLayout()
        self.__gridLay.setSpacing(10)
        self.__centralLay.addLayout(self.__gridLay)
        
        lId = QLabel("Numéro :")
        lFirstName = QLabel("Prénom :")
        lLastName = QLabel("Nom :")
        lLogin = QLabel("Login :")
        lPassword = QLabel("Mot de passe :")
        
        self.__edId = QLineEdit()
        self.__edId.setPlaceholderText("ID de l'utilisateur à modifier")
        
        self.__edFirstName = QLineEdit()
        self.__edFirstName.setPlaceholderText("Ex : Jean")
        
        self.__edLastName = QLineEdit()
        self.__edLastName.setPlaceholderText("Ex : Dupont")
        
        self.__edLogin = QLineEdit()
        self.__edLogin.setPlaceholderText("Ex : jdupont")
        
        self.__edPassword = QLineEdit()
        self.__edPassword.setPlaceholderText("••••••••")
        self.__edPassword.setEchoMode(QLineEdit.Password)
        
        if update:
            self.__gridLay.addWidget(lId, 0, 0, Qt.AlignRight)
            self.__gridLay.addWidget(self.__edId, 0, 1)
            
        self.__gridLay.addWidget(lFirstName, 1, 0, Qt.AlignRight)
        self.__gridLay.addWidget(self.__edFirstName, 1, 1)
        self.__gridLay.addWidget(lLastName, 2, 0, Qt.AlignRight)
        self.__gridLay.addWidget(self.__edLastName, 2, 1)
        self.__gridLay.addWidget(lLogin, 3, 0, Qt.AlignRight)
        self.__gridLay.addWidget(self.__edLogin, 3, 1)
        self.__gridLay.addWidget(lPassword, 4, 0, Qt.AlignRight)
        self.__gridLay.addWidget(self.__edPassword, 4, 1)
        
        # Boutons
        self.__buttonLay = QHBoxLayout()
        self.__buttonLay.addStretch()
        self.__centralLay.addLayout(self.__buttonLay)
        
        self.__butValid = QPushButton("Valider")
        self.__butAbort = QPushButton("Annuler")
        self.__buttonLay.addWidget(self.__butAbort)
        self.__buttonLay.addWidget(self.__butValid)
        
        self.__butAbort.clicked.connect(self.__ctrl.destroyUserEditUI)
        if update:
            self.__butValid.clicked.connect(self.__ctrl.updateUserProcess)
        else:
            self.__butValid.clicked.connect(self.__ctrl.createUserProcess)
        
        self.show()
    
    
    def getUser(self) -> User:
        '''!
        Permet de récupérer le user qui a été édité
        @return: User créé / modifié
        '''
        return User(
            self.__edFirstName.text(),
            self.__edLastName.text(),
            self.__edLogin.text(),
            self.__edPassword.text(),
            self.__edId.text()
        )