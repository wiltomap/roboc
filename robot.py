
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


    def save_position(self, coord):

        """Enregistre une position dans le fichier 'encours'.

        Si une partie est en cours, le fichier existe et comporte un
        objet liste nommé 'positions' qui stocke des tuples (x, y) correspondant
        aux positions successives du robot. Si non, il n'existe pas.

        NB : la lecture et l'écriture se font en mode binaire à
        l'aide du module pickle.

        """

        x, y = coord
        positions = list()

        try:
            with open("encours", "rb") as fichier:
                positions = pickle.load(fichier)
        except EOFError:
            os.remove("encours")
            # print("Fichier vide...")
        except FileNotFoundError:
            pass
            # print("Le fichier n'existe pas...")
        else:
            pass
            # print("Le fichier existe et contient {0}".format(positions))

        positions.append(coord)
        # print("La liste 'positions' contient desormais {0}".format(positions))

        with open("encours", "wb") as fichier:
            a = pickle.Pickler(fichier)
            a.dump(positions)
