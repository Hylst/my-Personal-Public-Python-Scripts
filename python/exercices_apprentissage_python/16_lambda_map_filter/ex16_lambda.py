# -*- coding: utf-8 -*-
"""
Exercice 16 : Lambda, Map, Filter, Reduce
Auteur : Geoffroy Streit
Date : Mai 2023

La programmation fonctionnelle, comme les runes des anciens !
"""

from functools import reduce

# ============================================================
# LAMBDA - Fonctions anonymes
# ============================================================

print("=== LAMBDA ===\n")

# Fonction classique
def doubler(x):
    return x * 2

# Équivalent lambda
doubler_lambda = lambda x: x * 2

print(f"Fonction: doubler(5) = {doubler(5)}")
print(f"Lambda: doubler_lambda(5) = {doubler_lambda(5)}")

# Lambda multi-arguments
calculer_degats = lambda base, mod, crit: (base + mod) * (2 if crit else 1)
print(f"\nDégâts normaux: {calculer_degats(10, 3, False)}")
print(f"Dégâts critiques: {calculer_degats(10, 3, True)}")

# ============================================================
# MAP - Appliquer une fonction à tous les éléments
# ============================================================

print("\n=== MAP ===\n")

jets = [8, 15, 3, 19, 12, 7]
print(f"Jets originaux: {jets}")

# Ajouter un bonus de +3
avec_bonus = list(map(lambda x: x + 3, jets))
print(f"Avec bonus +3: {avec_bonus}")

# Convertir en string
jets_str = list(map(str, jets))
print(f"En strings: {jets_str}")

# Équivalent comprehension (souvent préféré)
avec_bonus_comp = [x + 3 for x in jets]
print(f"Comprehension: {avec_bonus_comp}")

# ============================================================
# FILTER - Garder selon condition
# ============================================================

print("\n=== FILTER ===\n")

# Garder les réussites (>= 10)
reussites = list(filter(lambda x: x >= 10, jets))
print(f"Jets: {jets}")
print(f"Réussites (>=10): {reussites}")

# Garder les pairs
pairs = list(filter(lambda x: x % 2 == 0, jets))
print(f"Jets pairs: {pairs}")

# Équivalent comprehension
reussites_comp = [x for x in jets if x >= 10]
print(f"Comprehension: {reussites_comp}")

# ============================================================
# REDUCE - Réduire à une valeur
# ============================================================

print("\n=== REDUCE ===\n")

# Somme (exemple simple)
total = reduce(lambda a, b: a + b, jets)
print(f"Somme des jets: {total}")

# Produit
produit = reduce(lambda a, b: a * b, [2, 3, 4])
print(f"Produit [2,3,4]: {produit}")

# Trouver le max
maximum = reduce(lambda a, b: a if a > b else b, jets)
print(f"Maximum: {maximum}")

# ============================================================
# Combinaison - Le combo ultime
# ============================================================

print("\n=== COMBO MAP + FILTER + REDUCE ===\n")

# Somme des jets doublés qui sont >= 10
jets = [8, 15, 3, 19, 12, 7]
resultat = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x >= 10,
        map(lambda x: x * 2, jets)
    )
)
print(f"Jets: {jets}")
print(f"Doublés >= 10, sommés: {resultat}")

# Version lisible (souvent préférée)
resultat_lisible = sum(x * 2 for x in jets if x * 2 >= 10)
print(f"Version lisible: {resultat_lisible}")

print("\n✅ Exercice 16 terminé !")
