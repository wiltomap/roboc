"""Module contenant les fonctions nécessaires au programme."""

def references(chaine):

    """
    Renvoie deux objets :

        - Un dictionnaire mémorisant le contenu de chaque case de la
          carte passée en paramètre, sous la forme : { (0, 1): "O", ... }

        - Un tuple contenant les coordonnées (x,y) du robot

    NB : origine (0,0) située en haut à gauche de la grille

    """

    robot = tuple()
    grille = dict()

    chaine = chaine.split("\n")

    largeur = len(chaine[0])
    hauteur = len(chaine)

    for index_a, value_a in enumerate(chaine):
        for index_b, value_b in enumerate(value_a):
            grille[index_a, index_b] = value_b
            if value_b == "X":
                robot = (index_a, index_b)

    return grille, robot, largeur, hauteur


def calcul_position(depart, action):

    """
    Renvoie la nouvelle position du robot à partir des
    variables passées en paramètres :

        - depart : position initiale sous la forme d'un tuple (x,y)
        - action : action entrée par l'utilisateur (exemple : "e2")

    """

    x, y = (depart[0], depart[1])

    direction = action[0]

    vitesse = action[1:]

    if vitesse == "":
        vitesse = 1
    else:
        vitesse = int(vitesse)

    if direction == "o":
        x = x - vitesse
    elif direction == "e":
        x = x + vitesse
    elif direction == "n":
        y = y - vitesse
    elif direction == "s":
        y = y + vitesse
    else:
        pass

    if x < 0 or y < 0:
        return "Position ({0},{1}) hors-grille...".format(x, y)

    return (x, y)
