
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import FARM_NAME
from models.farm_model import FarmModel
from models.linear_program import LinearProgram
from solvers.simplex import SimplexSolver


def run_app():
    print(f"--- Welcome to the Optimization Tool: {FARM_NAME} ---\n")

    # Create and load farm
    farm = FarmModel(FARM_NAME)
    farm.load_default_data()
    print(f"✓ Farm loaded: {farm.name}")
    print(f"✓ Crops loaded: {', '.join([c.name for c in farm.crops])}\n")

    # Formulate linear program
    print("Formulating linear program...")
    lp = LinearProgram(farm)
    print(f"✓ Matrix A shape: {lp.A.shape}")
    print(f"✓ Vector c: {lp.c}")
    print(f"✓ Vector b: {lp.b}\n")

    # Solve
    print("Solving optimization problem...")
    solver = SimplexSolver(lp)
    solver.solve()
    result = solver.get_result()

    if result:
        print(f"✓ Solution found!\n")
        print(f"Maximum profit: {result['profit']:,.0f} DH/year\n")
        print("Optimal surface allocation:")
        for i, crop in enumerate(farm.crops):
            print(f"  x{i + 1} ({crop.name:10}) = {result['variables'][i]:6.2f} ha")
        print()
    else:
        print("❌ No solution found")

    print("--- Optimization Complete ---")


if __name__ == "__main__":
    run_app()