class Livre :

    #constructeur de la classe Livre
    def __init__(self, titre="" , auteur="" , nbPages=0 , disponible=True):
        self._titre = titre
        self._auteur = auteur 
        self._nbPages = nbPages
        self._disponible = disponible

    #creation des getters 
    def getTitre(self):
        return self._titre
    
    def getAuteur(self):
        return self._auteur
    
    def getNbPages(self):
        return self._nbPages
    
    def getDisponibilite(self):
        return self._disponible
    
    #creation des settres 
    def setTitre(self, new_titre):
        self._titre = new_titre

    def setAuteur(self, new_auteur):
        self._auteur = new_auteur

    def setNbPages(self, new_nbPages):
        if (type(new_nbPages) == int) and (new_nbPages>=0):
            self._nbPages = new_nbPages
        else :
            print("Erreur: La page du livre doit être un nombre entier positif.")

    
    def setDisponibilite(self, disponible):
        self._disponible = disponible

    #methode verefcation 
    def verefcation(self):
        if self.getDisponibilite() == True :
            return True 
        else:
            return False
        
    
    def emprunter (self):
        if self.verefcation()==True :
            self.setDisponibilite(False)
        else:
            print("le livre n'est actuellement pas disponible")

 
    #methode rendre 
    def rendre (self):
        if self.verefcation()==False :
            self.setDisponibilite(True)
        else:
            print("Le livre est déjà rendu ou n'a pas été empunter ")



#intancier la classe Livre 
L1 = Livre("la force de l'homme","Paolo" , 200)

#afficher le nom de livre 
print(f"Le titre de livre est : {L1.getTitre()}")

#afficher l'auteur de Livre 
print(f"L'auteur de ce livre est : {L1.getAuteur()}")

#afficher le nombre de page 
print(f"le nombre de page de ce livre est : {L1.getNbPages()}")


print("\nLes information de livre aprés les modifécations ")

#changer le nom de livre 
L1.setTitre("La Force du Vin")
print(f"le titre de ce livre est maintenant : {L1.getTitre()}")

#changer le nom de l'auteur 
L1.setAuteur("Vincent Van Gogh")
print(f"l'auteur de ce livre est maintenant : {L1.getAuteur()}")

#changer le nombre de page 
L1.setNbPages(-1)   ###nombre négatif
print(f"les pages de ce livre sont maintenant : {L1.getNbPages()}")

L1.setNbPages(23.56)   ###nombre réel 
print(f"les pages de ce livre sont maintenant : {L1.getNbPages()}")

L1.setNbPages(290)  ###nombre positif et entier 
print(f"les pages de ce livre sont maintenant : {L1.getNbPages()}")

print("\nverfier la disponilité d'un livre") 
print(f"livre {L1.getTitre()} , disponible ? : {L1.verefcation()}") 

print("\nemprunter le livre") 
L1.emprunter()
print(f"livre {L1.getTitre()} , disponible ? :{L1.verefcation()}")

print("\nrendre le livre") 
L1.rendre()
print(f"livre {L1.getTitre()} , disponible ? :{L1.verefcation()}")

print("\nrendre le livre sans l'emprunter")
L1.rendre()
