import re

class Patisserie:

    __createur = "ratatouille"

    def __init__(self, pd = 0, cat = None):
        self.__poids = pd
        self.__categorie = Patisserie.inttest(cat)
    
    

    def get_poids(self):
        return int(self.__poids)
    def get_categorie(self):
        return self.__categorie
    
    def set_poids(self, new_pd):
        self.__poids = new_pd
    def set_categorie(self, new_cat):
        self.__categorie = Patisserie.inttest(new_cat)
    @staticmethod
    def get_categorie_autorise():
        return ["gateau","tarte"]

    @classmethod
    def get_createur(cls):
        return cls.__createur
    @classmethod
    def set_createur(cls, new_crea):
        cls.__createur = new_crea

    def inttest(cat):
        if cat == None:
            return cat
        elif not re.search(r"^[A-Z][a-zA-Z ]*$", cat):
            return None
        else:
            return cat

    def __eq__(self,other):
        if self.get_poids()== other.get_poids():
            return True
        else:
            return False

    def __add__(self, other):
        if str(self.get_categorie()) == str(other.get_categorie()):
            return int(self.get_poids())+int(other.get_poids()), self.get_categorie()
        else:
            return int(self.get_poids())+int(other.get_poids()), None
    def __str__(self):
        return str(self.__poids)+" "+str(self.__categorie)

    def __del__(self):
        del self.__poids
        del self.__categorie
