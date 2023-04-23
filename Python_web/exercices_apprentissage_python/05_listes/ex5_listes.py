# -*- coding: utf-8 -*-
"""
Exercice 05 : Les Listes
Auteur : Geoffroy Streit
Date : Avril 2023

Les listes, c'est comme l'inventaire du héros - on y met tout !
"""

# ============================================================
# Création de listes - L'inventaire du héros
# ============================================================

# Liste simple
inventaire = ["épée", "bouclier", "potion", "torche"]
print("Mon inventaire:", inventaire)

# Liste de nombres - les stats
stats = [18, 14, 12, 10, 8, 15]
print("Stats du personnage:", stats)

# Liste mixte (même si c'est pas très propre)
perso = ["Gandalf", 150, True, 99.5]
print("Données perso:", perso)

# ============================================================
# Accès aux éléments - Comme fouiller son sac
# ============================================================

print("\n=== Accès aux éléments ===")
print(f"Premier objet: {inventaire[0]}")
print(f"Dernier objet: {inventaire[-1]}")  # Le -1 c'est pratique !
print(f"Objets 1 à 3: {inventaire[1:3]}")  # Slicing, très utile

# ============================================================
# Modification de liste - Gestion d'inventaire
# ============================================================

print("\n=== Modifications ===")

# Ajout d'objets
inventaire.append("corde")
print(f"Après append: {inventaire}")

inventaire.insert(0, "carte au trésor")  # Au début
print(f"Après insert: {inventaire}")

# Suppression
objet_utilise = inventaire.pop()  # Retire le dernier
print(f"Objet utilisé: {objet_utilise}")
print(f"Après pop: {inventaire}")

inventaire.remove("torche")  # Retire par valeur
print(f"Torche jetée: {inventaire}")

# ============================================================
# Opérations sur les listes
# ============================================================

print("\n=== Opérations ===")

degats = [12, 8, 15, 6, 20, 3]
print(f"Liste de dégâts: {degats}")
print(f"Somme: {sum(degats)}")
print(f"Max: {max(degats)}")
print(f"Min: {min(degats)}")
print(f"Longueur: {len(degats)}")

# Tri
degats_tries = sorted(degats)
print(f"Triés: {degats_tries}")

degats.sort(reverse=True)  # Tri en place, décroissant
print(f"Triés décroissant: {degats}")

# ============================================================
# Parcours de liste - Le tour de table
# ============================================================

print("\n=== Parcours ===")
equipe = ["Guerrier", "Mage", "Voleur", "Clerc"]

for membre in equipe:
    print(f"  🎭 {membre} rejoint l'aventure!")

# Avec index (enumerate c'est la vie)
print("\nAvec positions:")
for i, membre in enumerate(equipe):
    print(f"  Position {i}: {membre}")

# ============================================================
# Vérifications
# ============================================================

print("\n=== Vérifications ===")
if "Mage" in equipe:
    print("On a un mage, on peut lancer des sorts!")

if "Barde" not in equipe:
    print("Pas de barde... tant mieux, j'aime pas les chansons en combat 😅")

# ============================================================
# Fin exercice 5 - Les listes c'est vraiment pratique !
# ============================================================
