"""
 Modèle de données d'une ferme agricole
"""


from config import DEFAULT_RESOURCES, DEFAULT_CROPS


class Crop:
    def __init__(self, name, profit, water, budget, labor):
        self.name = name
        self.profit = profit
        self.water = water
        self.budget = budget
        self.labor = labor

    def __repr__(self):
        return (f"Crop(name='{self.name}', profit={self.profit} DH/ha, "
                f"water={self.water} L/ha)")


class FarmModel:
    def __init__(self, name):
        self.name = name
        self.crops = []          # ← "crops" pas "corps"
        self.resources = {}      # ← "resources" pas "ressources"

    def add_crop(self, crop):    # ← "add_crop" pas "add_corp"
        self.crops.append(crop)

    def load_default_data(self):
        """Charge les cultures et ressources depuis config.py"""
        self.resources = DEFAULT_RESOURCES

        for name, data in DEFAULT_CROPS.items():
            new_crop = Crop(
                name=name,
                profit=data["profit"],
                water=data["water"],
                budget=data["budget"],
                labor=data["labor"]
            )
            self.add_crop(new_crop)

    def __repr__(self):
        return f"FarmModel(name='{self.name}', crops={len(self.crops)})"