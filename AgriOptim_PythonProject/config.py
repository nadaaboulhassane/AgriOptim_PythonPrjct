# ============================================================
# config.py — Le "règlement interne" du projet AgriOptim
# ============================================================
# Ce fichier contient TOUTES les valeurs fixes du projet.
# Si tu veux changer un profit ou une ressource,
# tu ne touches QUE ce fichier.
# ============================================================

# --- Informations générales du projet ---
PROJECT_NAME  = "AgriOptim"
VERSION       = "1.0.0"
AUTHORS       = ["Nada ABOULHASSANE", "Mohamed Taha AJARROUD"]
INSTITUTION   = "EMSI"
ACADEMIC_YEAR = "2025-2026"

# --- Les cultures et leurs données ---
# Pour chaque culture on stocke :
#   profit  = ce qu'elle rapporte en DH par hectare cultivé
#   water   = eau qu'elle consomme (litres par hectare)
#   budget  = ce qu'elle coûte (DH par hectare)
#   labor   = heures de travail nécessaires par hectare
#   color   = couleur pour les graphiques (code hexadécimal)

FARM_NAME = "My Optimized Farm" # Tu peux mettre le nom que tu veux

DEFAULT_CROPS = {
    "blé": {
        "profit": 6000,
        "water":  300,
        "budget": 2000,
        "labor":  12,
        "color":  "#F4C430"
    },
    "maïs": {
        "profit": 4500,
        "water":  500,
        "budget": 2500,
        "labor":  18,
        "color":  "#228B22"
    },
    "légumes": {
        "profit": 7000,
        "water":  400,
        "budget": 3000,
        "labor":  15,
        "color":  "#FF6347"
    }
}

# --- Les ressources disponibles de la ferme ---
# C'est exactement les contraintes de ton rapport :
#   surface = 50 ha disponibles
#   water   = 20 000 litres d'eau
#   budget  = 110 000 DH
#   labor   = 720 heures de travail

DEFAULT_RESOURCES = {
    "surface": 50,
    "water":   20000,
    "budget":  110000,
    "labor":   720
}