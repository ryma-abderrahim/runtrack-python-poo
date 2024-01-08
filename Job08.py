import math 
class Cercle :
    def __init__ (self, rayon=0):
        self.rayon = rayon
    
    def changerRayon(self, new_rayon):
        self.rayon = new_rayon

    def afficherInfos (self):
        return f"le rayon de cercle :{self.rayon}"
    
    def circonference(self):
        return "{:.2f}".format(2 * math.pi * self.rayon)

    def aire (self):
        return "{:.2f}".format (math.pi * self.rayon ** 2)
    
    def diametre (self):
        return 2 * self.rayon
    

#intancier la classe cercle 
C1 = Cercle(4)

#affichage des informations de cercle C1
print("les informations du premier cercle sont:", C1.afficherInfos()) 

#changer le rayon de C1
C1.changerRayon(7)

#affichage des nouvelles informations de C1 après modification
print("les nouvelles informations du cercle sont :", C1.afficherInfos())

#afficher la circonférence  de C1
print ("la circonférence est ", C1.circonference(), "cm")

#afficher l'air de C1
print ("l'aire est ", C1.aire(), "cm²")

#afficher le diametre de C1
print("le diametre de cercle est", C1.diametre() )


#intancier la classe cercle 
C2= Cercle(7)

#affichage des informations de cercle C2
print("les informations du premier cercle sont:", C1.afficherInfos()) 

#changer le rayon de C2
C2.changerRayon(4)

#affichage des nouvelles informations de C2 après modification
print("les nouvelles informations du cercle sont :", C2.afficherInfos())

#afficher la circonférence  C2
print ("la circonférence est ", C2.circonference(), "cm")

#afficher l'air de C2
print ("l'aire est ", C2.aire(), "cm²")

#afficher le diametre  C2
print("le diametre de cercle est", C2.diametre() )