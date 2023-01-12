# Dans cet exercice, vous disposez d'une classe Entreprise qui contient un
# attribut de classe employes :

# class Entreprise:
#     employes = []
# Cet attribut est une liste qui doit contenir les employés de l'entreprise.

# Le but de cet exercice, est de créer des instances d'employés à partir de
# la liste de tuples employes :

# employes = [
#             ("Pierre", "Smith", "Responsable RH", 35000),
#             ("Julie", "Martin", "Développeur Python", 42000),
#             ("Éric", "Dupont", "Chef de projet", 50000),
#             ]
# Chaque instance d'employé créé à partir de la classe Employe doit être ajouté
# à l'attribut de classe employes de la classe Entreprise.

# L'attribut employes de la classe Entreprise, doit donc à la fin de l'exercice
# contenir trois instances de la classe Employe :

# >>> print(Entreprise.employes)
# [<__main__.Employe object at 0x102356860>,
#  <__main__.Employe object at 0x102356898>,
#  <__main__.Employe object at 0x1023568d0>]

class Entreprise:
    employes = []


class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire


employes = [
    ("Pierre", "Smith", "Responsable RH", 35000),
    ("Julie", "Martin", "Développeur Python", 42000),
    ("Éric", "Dupont", "Chef de projet", 50000),
]

# ////////////////////////////////////////////////////
for employe_data in employes:
    employe = Employe(*employe_data)
    print(employe_data)
    Entreprise.employes.append(employe)
# ////////////////////////////////////////////////////


# La première chose à faire pour pouvoir ajouter les employés contenus dans la
# liste employes est de boucler dessus pour avoir accès à chaque tuple de cette liste.

# Pour ce faire, on utilise une boucle for :

# for employe_data in employes:
# À l'intérieur de la boucle, on crée ensuite une instance à partir de la classe
# Employe :

# employe = Employe(*employe_data)
# Vous remarquerez que j'utilise l'astérisque, qui me permet d'unpacker automatiquement
# le tuple dans les paramètres de la méthode __init__.

# En effet, on aurait pu spécifier chaque argument séparément en récupérant les éléments
# dans le tuple mais c'est plus long à écrire :

# employe = Employe(employe_data[0], employe_data[1], employe_data[2], employe_data[3])
# Ou encore en spécifiant le nom des paramètres, pour un code plus clair
# (mais définitivement plus long à écrire !) :

# employe = Employe(prenom=employe_data[0],
#                   nom=employe_data[1],
#                   position=employe_data[2],
#                   salaire=employe_data[3])
# Vu que les éléments dans le tuple sont de le même ordre que les paramètres de
# la méthode __init__, on peut donc utiliser l'astérisque pour 'unpacker' ces éléments :

# employe = Employe(*employe_data)
# Il ne reste plus qu'à ajouter l'instance récupérée dans la variable employe à
# l'attribut employes de la classe Entreprise :


# Pour unpacker des éléments d'un tuple, on peut utiliser l'astérisque.

# Pour ajouter un élément à une liste, on utilise la méthode append.

# Pour boucler sur une liste, on utilise une boucle for.
