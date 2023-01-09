# Dans cet exercice, vous devez faire hériter la classe
# ListeCustom de la classe list de Python.

# On doit ainsi pouvoir utiliser la méthode append sur
# notre instance liste.

# Vous devez ajouter le nombre 5 à l'instance liste.

class ListeCustom(list):
    pass


liste = ListeCustom()
liste.append(5)

# Pour hériter d'une classe, il faut indiquer cette
# classe dans les parenthèses lors de la définition de
# la classe.
