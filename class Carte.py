class Carte:

    def __init__(self, nom, mana, description):
        self.nom= nom
        self.mana= mana
        self.description= description

from carte import Carte

class Cristal (Carte):
    
    def __init__(self, valeur):
        self.valeur= valeur 

from carte import Carte 

class Creature:

    def __init__(self, PV, Atk):
        self.PV= PV 
        self.Atk= Atk