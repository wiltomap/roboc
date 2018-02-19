
"""Ce module contient la classe Carte."""

def ref(chaine):

    """

    Renvoie deux informations sur la carte passée en paramètre :

    - La position du robot (x, y)
    - La position de la porte de sortie (x, y)
    - La liste des obstacles (liste : [ (1, 1), (1, 3), ...] )

    """

    robot = tuple()
    succes = tuple()
    obstacles = list()

    for index_a, value_a in enumerate(chaine.split("\n")):
        for index_b, value_b in enumerate(value_a):
            if value_b == "X":
                robot = (index_b, index_a)
            if value_b == "O":
                obstacles.append((index_b, index_a))
            if value_b == "U":
                succes = (index_b, index_a)

    return robot, succes, obstacles



class Carte:

    """

    Matérialise un fichier texte sous la forme d'un objet Carte.
    Une instance est créée à chaque nouvelle partie.

    Il comporte les attributs suivants :

        - self.nom :            nom de la carte
        - self.chaine :         chaine brute telle que lue dans le fichier *.texte
        - self.plan :           chaine brute sans le robot (plan)
        - self.position_robot : position initiale du robot sous la forme d'un tuple (x,y)
        - self.largeur :        nombre de colonnes
        - self.hauteur :        nombre de lignes

    """

    def __init__(self, nom, chaine):

        self.nom = nom
        self.chaine = chaine
        self.plan = chaine.replace("X", " ")
        self.robot = ref(chaine)[0]
        self.succes = ref(chaine)[1]
        self.obstacles = ref(chaine)[2]
        self.largeur = len(chaine.split("\n")[0])
        self.hauteur = len(chaine.split("\n"))


    def __repr__(self):
        return "<Carte {}>".format(self.nom)


    def grille(self, coord):

        """Renvoie la carte avec la position du robot passée en paramètre."""

        x, y = coord

        succes = False

        grille = self.plan.split("\n")
        destination = grille[y][x]

        grille[y] = list(grille[y])
        grille[y][x] = "X"
        grille[y] = "".join(grille[y])
        grille = "\n".join(grille)

        return grille
