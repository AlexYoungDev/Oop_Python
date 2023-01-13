# Dans cet exercice, vous devez créer une méthode
# changer_prix qui permette de modifier le prix de
# l'instance harry_potter :

# harry_potter.changer_prix(prix=14.99)
# Le prix de l'instance harry_potter doit être de 14.99
# à la fin du script.

# Le prix la classe Livre doit lui rester à 9.99.
class Livre:
    prix = 9.99

    def __init__(self, prix):
        self.prix = prix

# ///////////////////////////////////////////////////
    def changer_prix(self, prix):
        self.prix = prix
# ///////////////////////////////////////////////////


harry_potter = Livre(19.99)
harry_potter.changer_prix(prix=14.99)

print(harry_potter.prix)

# Pour créer une méthode, il faut utiliser la même syntaxe que pour une fonction.
# La seule chose à ne pas oublier est de mettre self en premier paramètre.

# self correspond à l'instance que nous manipulons, dans ce cas-ci harry_potter.

# Quand nous appelons la méthode changer_prix sur l'instance harry_potter,
# Python passe en fait par la classe.

# Les deux lignes de codes suivantes sont les même et la deuxième façon de faire
# vous montre bien que l'instance est envoyée en argument au paramètre self de
# la méthode changer_prix :

# harry_potter.changer_prix(prix=14.99)

# # En arrière-plan, Python opère comme ceci, d'où la nécessité de mettre self
# # en premier paramètre pour récupérer l'instance.
# Livre.changer_prix(self=harry_potter, prix=14.99)
# La méthode changer_prix doit également accepter un deuxième paramètre qui va
# récupérer le nouveau prix que l'on souhaite attribuer à l'attribut prix de
# l'instance :

# On assigne ensuite la valeur récupérée par ce paramètre prix à l'attribut
# d'instance self.prix :

# def changer_prix(self, prix):
#     self.prix = prix
# On a donc à la fin du script l'attribut Livre.prix qui reste inchangé à 9.99.

# La valeur de harry_potter.prix elle a cependant été modifiée par l'appel de
# la méthode changer_prix :

# harry_potter.changer_prix(prix=14.99)


# Pour créer une méthode, on utilise la même syntaxe que
# pour créer une fonction, avec l'instruction def.

# Il ne faut pas oublier de mettre le paramètre self en
# premier paramètre de la méthode pour récupérer l'instance.
