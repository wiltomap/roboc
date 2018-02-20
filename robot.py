
"""Ce module contient la classe Robot."""

import pickle


class Robot:

    """Classe désignant un robot.

    Gère les coordonnées du robot et sauvegarde chaque
    nouvelle position dans le fichier 'encours'.

    """

    def __init__(self, coord):

        self.coord = coord


    def set_position(self, action):

        """
        Renvoie la nouvelle position du robot à partir des
        variables passées en paramètres :

            - depart : position initiale sous la forme d'un tuple (x,y)
            - action : action entrée par l'utilisateur (exemple : "e2")

        """

        x, y = self.coord[0], self.coord[1]

        direction, vitesse = action[0], action[1:]

        vitesse = 1 if vitesse == "" else int(vitesse)

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

        return x, y


    def save_position(self, coord, coord_succes, nom_carte):

        """Enregistre une position dans le fichier 'encours'.

        Si une partie est en cours, le fichier comporte un objet
        dictionnaire qui stocke en clé le nom de la carte et en valeur
        la dernière position du robot : { "carte": (x, y), ... }.

        NB : la lecture et l'écriture se font en mode binaire à
        l'aide du module pickle.

        """

        x, y = coord
        positions = dict()

        with open("encours", "rb") as fichier:
            positions = pickle.load(fichier)

        if coord == coord_succes:
            del positions[nom_carte]
        else:
            positions[nom_carte] = coord

        with open("encours", "wb") as fichier:
            a = pickle.Pickler(fichier)
            a.dump(positions)
