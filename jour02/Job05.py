class Voiture :

    def __init__(self, marque="", modele="", annee=0, KM=0, en_marche=False , reservoir=50):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._KM = KM
        self._en_marche = en_marche
        self._reservoir= reservoir

    #getters and setters 
    def getMarque(self):
        return self._marque
    
    def setMarque(self, new_marque):
        self._marque=new_marque

    def getModele(self):
        return self._modele
    
    def setModele(self, new_modele):
        self._modele = new_modele

    def getAnnee(self):
        return self._annee
    
    def setAnnee(self, new_annee):
        self._annee=new_annee
    
    def getKM(self):
        return self._KM
    
    def setKM(self,new_KM):
        self._KM = new_KM
    
    def getEnMarche(self):
        return self._en_marche
    
    def setEnMarche(self, new):
        self._en_marche=new 
    
    
    def verfier_plein(self):
        return self._reservoir


    def demarrer (self):
        if self.verfier_plein() >5 :
            print("Le vehicule est en marche")
            self._en_marche =True
        
        else:
            print ("Votre reservoir de carburant est vide.")



    def arreter (self):
        if self.getEnMarche():
            print("Le véhicule est éteint.")
            self.setEnMarche(False)
        else:
            print("Impossible d'arrêter le véhicule : il était déjà en arret")
            
        
   
#istance of the class Voiture 
V1=Voiture("Pegeot","206",2014 , 13000 ,False , 5)
print(f"la marque : {V1.getMarque()}")
print(f"le modèle :{V1.getModele()}")
print(f"l'année : {V1.getAnnee()} ")
print(f"La consommation du Km : {V1.getKM()}")
V1.demarrer()
V1.arreter()

V2=Voiture("TOYOTA","500",2014 , 13000 ,True , 40)
print(f"la marque : {V2.getMarque()}")
print(f"le modèle :{V2.getModele()}")
print(f"l'année : {V2.getAnnee()} ")
print(f"La consommation du Km : {V2.getKM()}")
V2.demarrer()
V2.arreter()


