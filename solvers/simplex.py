from scipy.optimize import linprog
import numpy as np

class SimplexSolver:
    def __init__(self, lp):  # lp = linear program
        self.lp = lp
        self.result = None

    def solve(self):
        # scipy minimise par défaut, donc on négative c pour maximiser
        self.result = linprog(
            c = self.lp.c,      # négative car on maximise
            A_ub = self.lp.A,    # matrice des contraintes
            b_ub = self.lp.b,    # vecteur des limites
            method = 'highs'
        )

    def get_result(self):
        # D'abord on vérifie que result existe ET que ça a réussi
        if self.result is not None and self.result.success:
            return {
                "variables": self.result.x,         # surfaces optimales
                "profit": -self.result.fun,         # on re-négative
                "status": self.result.message       # message de succès
            }
        return None