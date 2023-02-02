# Dans cet exercice, vous devez faire hériter la classe
# Cube de la classe Shape.

# Vous devez en plus vous assurer que la classe Cube
# hérite des attributs d'instance définis dans la classe
# Shape (les attributs x et y de la méthode __init__).

# Comme un cube est en trois dimensions, vous devez en plus
# ajouter un attribut z qui n'existera que sur les instances
# de la classe Cube et non pas sur la classe Shape.

# Les trois attributs x, y et z doivent être définis à 0.
class Shape:
    def __init__(self):
        self.x = 0
        self.y = 0

# ///////////////////////////////////////////////////


class Cube(Shape):
    def __init__(self):
        super().__init__()
        self.z = 0
# ///////////////////////////////////////////////////


cube = Cube()
print(cube.x)
print(cube.y)
print(cube.z)


# La première chose à faire était de rajouter le nom de la classe Shape à
# l'intérieur des parenthèses de la classe Cube pour que Cube hérite de Shape.

# class Cube(Shape):
# Pour que les attributs x et y soient accessibles sur les instances de Cube,
# il faut appeler la méthode __init__ de la classe parente (la classe Shape)
# dans laquelle ces attributs sont définis :

# class Cube(Shape):
#     def __init__(self):
#         super().__init__()
# Depuis Python 3, vous pouvez utiliser la fonction "super" en l'appelant directement
# sans lui passer aucun argument :

# super()

# Pour finir, il fallait créer un attribut z uniquement sur les instances de la
# classe Cube.

# Pour cela, on crée un attribut z à l'intérieur de la méthode __init__ de la
# classe Cube :

# def __init__(self):
#     super().__init__()
#     self.z = 0
# ⚠️ Il ne fallait pas ajouter l'attribut à la suite des attributs x et y de la
# classe Shape, car on ne voulait ajouter cet attribut que pour les instances de la
# classe Cube.


# Pour appeler une méthode de la classe parent, on peut utiliser la fonction super.
