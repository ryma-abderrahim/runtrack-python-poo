class Tache :
    def __init__(self, titre, descreption, statut="à faire"):
        self._titre = titre
        self._description = descreption
        self._statut = statut

    
    #getters and setters
    def getTitre(self):
        return self._titre
    
    def setTitre(self, new_titre):
        self._titre = new_titre

    def getDescreption (self):
        return self._descripion
    
    def setDescreption(self , new_descreption):
        self._descripion = new_descreption

    def getStatus(self):
        return self._statut
    
    def setStatut(self,new_status):
        if new_status in [ "terminé","à faire"]:
            self._statut=new_status



################################class ListeDeTache##############################
class ListeDeTaches :

    def __init__(self):
        self._taches = []  


    def ajouterTache(self , new_tache):
        #ajoute une nouvelle tâche à la fin de la liste
        if isinstance(new_tache, Tache):   
            self._taches.append(new_tache)
        else:
            print("La tache doit être un objet Tache")
    

    def supprimerTache(self , Tache):
        self._taches.remove(Tache)

    def marquerCommeFinie(self, Tache):
        for t in  self._taches :
            if t._titre == Tache._titre :
                t.setStatut('terminé')

    def afficherListe(self):
        for tache in self._taches:
            print(f"Titre : {tache._titre}, Description : {tache._description}, Statut : {tache._statut}")

    def filterListe (self , statut):
        tache_filtrer=[]
        for tache in self._taches :
            if tache._statut == statut :
                tache_filtrer.append(tache)
        return tache_filtrer
    

#creation des instances
tache1=Tache("cours","faire les exercices et préparer les cours","à faire")
tache2=Tache("manger","aller acheter du pain et du fromage","à faire")
tache3=Tache("sport","aller au sport demain matin","à faire")
tache4=Tache("preparation" , "préparer son sepeetch pour le soft Skills","à faire")
tache5=Tache("ménage","néttoyer la chambre","terminée")

listeDesTaches=ListeDeTaches()
listeDesTaches.ajouterTache(tache1)
listeDesTaches.ajouterTache(tache2)
listeDesTaches.ajouterTache(tache3)
listeDesTaches.ajouterTache(tache4)
listeDesTaches.ajouterTache(tache5)

print("\nAffichage de la liste complète")
listeDesTaches.afficherListe()

print("\nFiltre sur 'à faire' ")
filterAFaire = ListeDeTaches()
filterAFaire = listeDesTaches.filterListe ('à faire')
print(f"Tache à faire :")
for tache in filterAFaire:
    print(tache.getTitre())


print("\nMarquage de la tâche 'manger' comme 'terminée' ")
listeDesTaches.marquerCommeFinie(tache2)

print("Affichage de la liste après modification")
listeDesTaches.afficherListe()

print("\n suprimmer la manger ")
listeDesTaches.supprimerTache(tache2)

print("Affichage de la liste après modification")
listeDesTaches.afficherListe()

