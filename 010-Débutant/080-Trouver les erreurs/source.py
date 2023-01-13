# Dans cet exercice, vous devez modifier le code de base
# pour qu'il ne retourne plus d'erreur et qu'il affiche
# les coordonnées x, y et z de l'instance sphere avec des
# valeurs respectivement de 9, 2 et 5 (pour x, y et z).

# Votre script doit donc afficher :

# 9
# 2
# 5
class Geometry:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


sphere = Geometry(x=9, y=2, z=5)
print(sphere.x)
print(sphere.y)
print(sphere.z)


# Premièrement, il faut corriger la méthode init à laquelle
# il manquait les deux tirets de bas avant et après le mot
# init.

# Sans ces tirets du bas, la méthode n'est pas appelée
# automatiquement lors de l'instanciation de la classe
# et les attributs ne sont donc pas définis.

# class Geometry:
# 	def __init__(self, x=0, y=0):
# Ensuite, il fallait modifier la variable pos_x qui
# n'existe pas et qui vous retournait une erreur de
# type NameError. À la place, il fallait donc mettre x,
# qui est le nom du paramètre défini dans la méthode
# __init__ :

# def __init__(self, x=0, y=0):
#     self.x = x
#     self.y = y
#     self.z = z
# Il fallait également ajouter un paramètre à la
# méthode __init__ pour pouvoir récupérer la valeur 5
# qui est envoyée au paramètre z lors de la création
# de l'instance sphere.

# On joute donc un paramètre z avec une valeur par
# défaut de 0 comme pour les autres coordonnées et
# on assigne la valeur de z à l'attribut self.z :

# def __init__(self, x=0, y=0, z=0):
#     self.x = x
#     self.y = y
#     self.z = z
# Pour finir, il fallait rajouter les parenthèses lors
# de la création de l'instance sphere et donner les
# valeurs 9, 2 et 5 respectivement aux paramètres x,
# y et z :

# sphere = Geometry(x=9, y=2, z=5)
