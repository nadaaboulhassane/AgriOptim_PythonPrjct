import numpy as np  # biblio des calculs


class LinearProgram:
    def __init__(self, farm):
        self.farm = farm
        """on va creer une matrice pour le calcul linéaire"""
        self.c = None  # vecteur de ce qu'on veut maximiser
        self.A = None  # la matrice: combien chaque plante consomme
        self.b = None  # vecteur des limites, le max d'eau etc (ressources)
        self.build_matrices()  # appeler la fonction tout de suite

    def build_matrices(self):
        """construire les matrices C, A et B"""

        # Créer les listes vides
        profits_list = []
        surfaces = []
        waters = []
        budgets = []
        labors = []

        # UNE SEULE boucle pour remplir toutes les listes
        for crop in self.farm.crops:
            profits_list.append(crop.profit)
            surfaces.append(1)  # Chaque culture occupe 1 hectare
            waters.append(crop.water)
            budgets.append(crop.budget)
            labors.append(crop.labor)

        # Après la boucle, créer les matrices
        # la biblio scipy minimise auto, donc on multiplie par -1 pour maximiser
        self.c = np.array(profits_list) * -1

        # pour A - la matrice de consommation
        self.A = np.array([surfaces, waters, budgets, labors], dtype=float)

        # pour B - les limites des ressources
        self.b = np.array([
            self.farm.resources["surface"],
            self.farm.resources["water"],
            self.farm.resources["budget"],
            self.farm.resources["labor"]
        ], dtype=float)