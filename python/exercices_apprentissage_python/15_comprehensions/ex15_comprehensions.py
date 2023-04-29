# -*- coding: utf-8 -*-
"""
Exercice 15 : List & Dict Comprehensions
Auteur : Geoffroy Streit
Date : Mai 2023

La magie Python en une ligne - comme un sort bien formulé !
"""

# ============================================================
# List Comprehensions - Le pouvoir en une ligne
# ============================================================

print("=== LIST COMPREHENSIONS ===\n")

# Méthode classique (boucle)
degats_classique = []
for i in range(1, 11):
    degats_classique.append(i * 2)
print(f"Méthode classique: {degats_classique}")

# Comprehension - même résultat, une ligne !
degats = [i * 2 for i in range(1, 11)]
print(f"Comprehension: {degats}")

# Avec condition - ne garder que les critiques (>15)
jets = [3, 18, 7, 20, 12, 19, 5, 16]
critiques = [j for j in jets if j >= 18]
print(f"\nJets: {jets}")
print(f"Critiques (>=18): {critiques}")

# Transformation + condition
bonus_critiques = [j * 2 for j in jets if j >= 15]
print(f"Jets doublés (si >=15): {bonus_critiques}")

# Nested comprehension - comme les donjons à étages
plateau = [[f"({x},{y})" for x in range(3)] for y in range(3)]
print(f"\nPlateau 3x3:")
for ligne in plateau:
    print(f"  {ligne}")

# ============================================================
# Dict Comprehensions - Le grimoire en une ligne
# ============================================================

print("\n=== DICT COMPREHENSIONS ===\n")

# Stats de base vers modificateurs D&D
stats = {"FOR": 16, "DEX": 14, "CON": 12, "INT": 18, "SAG": 10, "CHA": 8}
modificateurs = {stat: (val - 10) // 2 for stat, val in stats.items()}
print(f"Stats: {stats}")
print(f"Modificateurs: {modificateurs}")

# Filtrer un dict - que les stats positives
stats_fortes = {s: v for s, v in stats.items() if v >= 14}
print(f"Stats fortes: {stats_fortes}")

# Inverser clé/valeur
inventaire = {"épée": 1, "potion": 5, "or": 100}
inverse = {v: k for k, v in inventaire.items()}
print(f"\nInventaire inversé: {inverse}")

# ============================================================
# Set Comprehensions - Collection unique
# ============================================================

print("\n=== SET COMPREHENSIONS ===\n")

mots = ["gobelin", "dragon", "GOBELIN", "orc", "Dragon"]
mots_uniques = {m.lower() for m in mots}
print(f"Mots (originaux): {mots}")
print(f"Mots (uniques, minuscules): {mots_uniques}")

# ============================================================
# Comparaison performances
# ============================================================

print("\n=== POURQUOI C'EST MIEUX ? ===")
print("1. Plus lisible (une fois qu'on a compris)")
print("2. Plus rapide (optimisé en C sous le capot)")
print("3. Plus 'Pythonique' - le MJ approuve !")

print("\n✅ Exercice 15 terminé !")
