"""
 Gestion de l'affichage console
"""


def print_header():
    print("\n" + "=" * 60)
    print("  🌾 AgriOptim — Optimisation Agricole")
    print("=" * 60 + "\n")


def print_solution(farm, lp, solver):
    result = solver.get_result()
    if not result:
        print("❌ Pas de solution trouvée")
        return

    print(f"\n✅ Solution optimale trouvée !")
    print(f"\nProfit maximal : {result['profit']:,.0f} DH/an\n")
    print("Allocation des surfaces :")
    for i, crop in enumerate(farm.crops):
        print(f"  x{i + 1} ({crop.name:10}) = {result['variables'][i]:6.2f} ha")
    print()