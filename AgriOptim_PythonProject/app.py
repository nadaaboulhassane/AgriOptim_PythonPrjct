"""ghir bach iban lina result st3mlna lbiblio flask """

"""
app.py — Interface web Flask pour AgriOptim avec étapes
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, render_template, jsonify
from models.farm_model import FarmModel
from models.linear_program import LinearProgram
from solvers.simplex import SimplexSolver

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/optimize', methods=['GET'])
def optimize():
    """API endpoint pour résoudre l'optimisation étape par étape"""

    try:
        # ÉTAPE 1 : Charger la ferme
        farm = FarmModel("My Optimized Farm")
        farm.load_default_data()

        farm_info = {
            "name": farm.name,
            "crops": [
                {
                    "name": crop.name,
                    "profit": crop.profit,
                    "water": crop.water,
                    "budget": crop.budget,
                    "labor": crop.labor
                }
                for crop in farm.crops
            ],
            "resources": farm.resources
        }

        # ÉTAPE 2 : Formuler le programme linéaire
        lp = LinearProgram(farm)

        formulation = {
            "objective": "Max Z = 6000·x1 + 4500·x2 + 7000·x3",
            "constraints": [
                "Surface    : x1 + x2 + x3 ≤ 50",
                "Water      : 300·x1 + 500·x2 + 400·x3 ≤ 20000",
                "Budget     : 2000·x1 + 2500·x2 + 3000·x3 ≤ 110000",
                "Labor time : 12·x1 + 18·x2 + 15·x3 ≤ 720"
            ],
            "non_negativity": "x1, x2, x3 ≥ 0",
            "variables": "x1 = wheat (ha), x2 = corn (ha), x3 = vegetables (ha)"
        }

        # ÉTAPE 3 : Résoudre
        solver = SimplexSolver(lp)
        solver.solve()
        result = solver.get_result()

        if result is None:
            return jsonify({"error": "No solution found"}), 400

        # ÉTAPE 4 : Préparer les résultats
        allocation_data = [
            {
                "crop": crop.name,
                "hectares": float(result['variables'][i]),
                "revenue": float(result['variables'][i] * crop.profit),
                "profit_per_ha": crop.profit
            }
            for i, crop in enumerate(farm.crops)
        ]

        # Calculer les conseils
        advice = generate_advice(farm, result)

        # Retourner tout
        return jsonify({
            "farm": farm_info,
            "formulation": formulation,
            "profit": float(result['profit']),
            "allocation": allocation_data,
            "advice": advice
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def generate_advice(farm, result):
    """Générer des conseils basés sur la solution"""
    advice = []
    total_hectares = sum(result['variables'])

    # Conseil 1 : Utilisation des terres
    if total_hectares < farm.resources["surface"] * 0.8:
        advice.append({
            "icon": "⚠️",
            "title": "Underutilized Land",
            "message": f"You're using only {total_hectares:.1f} out of {farm.resources['surface']} hectares. Consider investing in additional resources."
        })
    else:
        advice.append({
            "icon": "✅",
            "title": "Land Usage",
            "message": f"Excellent! You're efficiently using {total_hectares:.1f}/{farm.resources['surface']} hectares."
        })

    # Conseil 2 : Diversification
    crops_planted = sum(1 for x in result['variables'] if x > 0.1)
    if crops_planted == 1:
        advice.append({
            "icon": "⚠️",
            "title": "Low Diversification",
            "message": "You're growing only one crop. Consider diversifying to reduce risk."
        })
    elif crops_planted == len(farm.crops):
        advice.append({
            "icon": "✅",
            "title": "Good Diversification",
            "message": f"Great! You're growing all {crops_planted} crops for balanced risk."
        })

    # Conseil 3 : Profit
    advice.append({
        "icon": "💰",
        "title": "Annual Revenue",
        "message": f"Your optimized farm will generate {result['profit']:,.0f} DH annually."
    })

    return advice


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)