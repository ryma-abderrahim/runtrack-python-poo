class CompteBancaire : 
    def __init__(self, numCompte , nom , prenom , solde, decouvert):
        self.__numCompte = numCompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    #getters and setters 
    def getNum(self):
        return self.__numCompte
    
    def setNum(self, new_num):
        self.__numCompte = new_num

    def getNom(self):
        return self.__nom
    
    def setNom(self, new_nom):
        self.__nom = new_nom

    def getPrenom(self):
        return self.__prenom
    
    def setPrenom(self, new_prenom):
        self.__prenom = new_prenom

    def getSolde(self):
        return self.__solde
    
    
    def setSolde(self,new_solde):
        if new_solde <0:
            print("Le solde ne peut pas etre negatif")
        else:
            self.__solde = new_solde


    def afficher (self):
        print("Numéro de compte : ", self.getNum())
        print("Nom : ", self.getNom()  ,self.getPrenom())
        print("Solde : ", self.getSolde(),"euros")


    def afficherSolde(self):
        return self.getSolde()


    def versement(self, montant):
        if montant <=0:
            print("Versement incorrect")
        else:
            self.__solde += montant


    def retrait  (self , montant):
        if montant<=0:
            print("Le montant du retrait est incorrect")
        else:
            if montant > self.getSolde():
                print("Le montant du retrait est supérieur au solde")
            else:
                self.__solde-=montant
     
    def agios(self):
        if self.__solde < 0:
            agios_a_appliquer = -0.5 * self.__solde
            self.__solde += agios_a_appliquer
            print(f"Solde actuelle :{self.getSolde()}")
        else :
            print("Les agios ne peuvent pas etre appliquer à ce compte ")
    
    def virement(self, obj , montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            obj.versement(montant)
            print(f"Virement de {montant} effectué avec succès vers le compte {obj.getNum()}.")
        else:
            print("Solde insuffisant et découvert non autorisé.")

#creation des compte 
cmpt=CompteBancaire(3987746,"John", "Doe" , 2000,True)

cmpt.afficher()
cmpt.versement(399)
print("\nApres le versement")
print(f"le montant actuelle de {cmpt.getNom()} {cmpt.getPrenom()} est de :{cmpt.getSolde()} euros")
cmpt.retrait(1200)
print("\nAprés le retrait")
print(f"le montant actuelle de {cmpt.getNom()} {cmpt.getPrenom()} est de : {cmpt.getSolde()} euros")

print("\n")
cmpt2=CompteBancaire(5667746,"Danny", "Doe" ,-563 , True)
cmpt2.afficher()


print("\n appliquation des agios:")
cmpt2.agios()


cmpt.virement(cmpt2,1199)
print("\nAprés le virement")
print(f"le montant actuelle de {cmpt2.getNom()} {cmpt2.getPrenom()} est de : {cmpt2.getSolde()} euros")
print(f"le montant actuelle de {cmpt.getNom()} {cmpt.getPrenom()} est de : {cmpt.getSolde()} euros")


