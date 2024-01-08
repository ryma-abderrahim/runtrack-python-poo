class Produit :
    
    def __init__(self, nom ="" , prixHT=0 , TVA=0):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA  

    def CalculerPrixTTC (self):
        return self.prixHT + (self.prixHT * (self.TVA/100))
    
    #methode pour changer le prix 
    def changerPrix(self, new_PrixHT):
        self.prixHT = new_PrixHT
    
    #methode pour changer le nom 
    def changerNom(self, new_nom):
        self.nom = new_nom

    #methode pour afficher le prix 
    def afficherPrix(self):
        return f"le prix Hors Taxe est : {self.prixHT}"
    
    #methode pour afficher le nom de produit 
    def afficherNom (self):
        return f"Le Nom du produit est : {self.nom} "
    
    def afficherPrixTTC(self):
        return f"Le Prix TTC est :{self.CalculerPrixTTC()}"
    

    def afficher(self):
        return f"le nom de produit : {self.nom} \nle prix hors taxe : {self.prixHT} \nla TVA :{self.TVA} \nLe Prix TTC de produit : {self.CalculerPrixTTC()}"                              

#Intancier la classe Produit
P1 = Produit("Téléphone",300, 10)
P2 = Produit("Télévesion", 1000, 10)
P3 = Produit("Casque de musique" ,90 , 11)

#afficher les information de chaque produit 
print ("Informations sur le téléphone")
print(P1.afficher())

print ("Informations sur la Télévison ")
print(P2.afficher())

print("Information sur les casque de musique ")
print(P3.afficher())

#Modification des noms et de prix des produits 
P1.changerNom("Smartphone Samsung")
P1.changerPrix(500)

#Affichage des nouvelles informations des produits
print("\n Nouvelles Informations \n")
print(P1.afficherNom())
print(P1.afficherPrix())
print(P1.afficherPrixTTC)