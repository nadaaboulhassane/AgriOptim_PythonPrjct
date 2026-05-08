"""
 Visualisation des résultats
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_allocation(farm, solver):
    result = solver.get_result()
    if not result:
        return

    names = [crop.name for crop in farm.crops]
    values = result['variables']

    plt.figure(figsize=(10, 5))
    plt.bar(names, values, color=['#F4C430', '#228B22', '#FF6347'])
    plt.ylabel('Hectares')
    plt.title('Allocation optimale des surfaces')
    plt.tight_layout()
    plt.show()