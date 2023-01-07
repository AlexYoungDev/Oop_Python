# Dans cet exercice, vous devez créer une classe Employe
# qui permettra de créer des employés qui auront
# 4 attributs :

# prenom
# nom
# position
# salaire

# On doit donc pouvoir avec votre script créer une
# instance de la sorte :

# john = Employe("John", "Smith", "Développeur Python", 45000)

class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire
