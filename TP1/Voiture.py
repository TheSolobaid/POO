class voiture:
    def __init__(self, marque = "Renau", model = "KANGOO", cheveaux = "87", couleur = "bleu chiotte mais po terni", option = []):
        self.__marque = marque
        self.__model = model
        self.__cheveaux = cheveaux
        self.__couleur = couleur
        self.__option = option


    def get_marque(self):
        return self.__marque

    def get_model(self):
        return self.__model

    def get_cheveaux(self):
        return self.__cheveaux

    def get_couleur(self):
        return self.__couleur
    
    def get_option(self):
        return self.__option


    def set_marque(self, new_marque):
        self.__marque = new_marque

    def set_model(self, new_model):
        self.__model = new_model

    def set_cheveaux(self, new_cheveaux):
        self.__cheveaux = new_cheveaux
    
    def set_couleur(self, new_couleur):
        self.__couleur = new_couleur
    
    def set_option(self, new_option):
        self.__option = new_option
    

    def  ajouter_option(self, opts):
        self.__option.append(opts)
    
    def supprimer_option(self, opt):
        self.__option.remove(opt)

    def is_option_present(self, opt):
        if opt in self.__option:
            return True

    def __str__(self) -> str:
        return  str(self.__marque)+" "+ str(self.__model)+" "+ str(self.__cheveaux)+" "+ str(self.__couleur)+" "+ str(self.__option)

    def __del__(self):
        del self.__marque
        del self.__model
        del self.__cheveaux
        del self.__couleur
        del self.__option