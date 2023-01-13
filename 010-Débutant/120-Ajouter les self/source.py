# Dans cet exercice, vous devez corriger le code pour
# qu'il fonctionne.

# La seule chose que vous devez rajouter, c'est le
# fameux self, qui pose beaucoup de problèmes aux débutants
# en programmation orientée objet.

# C'est le seul mot que vous devez ajouter.

# Le script final doit contenir self à 6 endroits différents.

# x, y et z doivent appartenir à l'instance mon_cube.

# À la fin du script, la valeur de l'attribut x de
# l'instance mon_cube doit être égale à 6 (pour valider
# l'exercice, la méthode move_x doit donc fonctionner et
# vous ne devez pas enlever la dernière ligne du script).
class Cube:
    def __init__(self, x=5, y=2, z=7):
        self.x = x
        self.y = y
        self.z = z

    def move_x(self):
        self.x += 1


mon_cube = Cube()
mon_cube.move_x()

# La première chose à laquelle il faut penser quand on
# crée des méthodes, c'est de toujours ajouter self comme
# premier paramètre.

# Il fallait donc ajouter self à la méthode __init__ et
# à la méthode move_x :

# class Cube:
#     def __init__(self, x=5, y=2, z=7):
#         x = x
#         y = y
#         z = z

#     def move_x(self):
#         x += 1


# mon_cube = Cube()
# mon_cube.move_x()


# Enfin, il fallait associer les attributs x, y et z
# à l'instance mon_cube.

# Pour cela, il fallait préfixer chaque variable par self.
# self représente l'instance (donc mon_cube dans ce cas-ci).

# On peut ainsi accéder à self.x à l'intérieur de la méthode
# move_x et incrémenter sa valeur de 1 :

# class Cube:
#     def __init__(self, x=5, y=2, z=7):
#         self.x = x
#         self.y = y
#         self.z = z

#     def move_x(self):
#         self.x += 1


# mon_cube = Cube()
# mon_cube.move_x()
