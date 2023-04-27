# -*- coding: utf-8 -*-
"""
Exercice 06 : Tuples et Ensembles
Auteur : Geoffroy Streit
Date : Avril 2023

Tuple = immuable, comme les règles sacrées du D&D !
Set = unique, comme les pièces de collection
"""

# ============================================================
# TUPLES - Les constantes du jeu
# ============================================================

print("=== TUPLES ===\n")

# Création de tuples
coordonnees = (5, 3)  # Position sur la carte
stats_base = (10, 10, 10, 10, 10, 10)  # FOR, DEX, CON, INT, SAG, CHA

print(f"Position du héros: {coordonnees}")
print(f"Stats de base: {stats_base}")

# Accès aux éléments (comme les listes)
print(f"Coordonnée X: {coordonnees[0]}")
print(f"Coordonnée Y: {coordonnees[1]}")

# Unpacking - super pratique !
x, y = coordonnees
print(f"Unpacking: x={x}, y={y}")

force, dex, con, intel, sag, cha = stats_base
print(f"Force: {force}, Intelligence: {intel}")

# Tuple dans fonction - retour multiple
def lancer_attaque():
    import random
    touche = random.randint(1, 20)
    degats = random.randint(1, 8)
    return (touche, degats)  # Retourne un tuple

resultat = lancer_attaque()
print(f"\nRésultat attaque: touche={resultat[0]}, dégâts={resultat[1]}")

# Ou directement avec unpacking
hit, dmg = lancer_attaque()
print(f"Avec unpacking: touche={hit}, dégâts={dmg}")

# ============================================================
# SETS (Ensembles) - Collection sans doublons
# ============================================================

print("\n=== SETS (Ensembles) ===\n")

# Création
competences = {"magie", "combat", "furtivité", "diplomatie"}
print(f"Compétences: {competences}")

# Les doublons sont automatiquement supprimés
inventaire_bordel = {"épée", "potion", "épée", "potion", "bouclier"}
print(f"Inventaire nettoyé: {inventaire_bordel}")  # Que 3 éléments !

# Ajout et suppression
competences.add("alchimie")
print(f"Après ajout: {competences}")

competences.discard("diplomatie")  # Discard ne plante pas si absent
print(f"Après suppression: {competences}")

# ============================================================
# Opérations ensemblistes - Le vrai pouvoir des sets
# ============================================================

print("\n=== Opérations ensemblistes ===")

classe_guerrier = {"combat", "endurance", "armure lourde", "intimidation"}
classe_mage = {"magie", "concentration", "arcanes", "intimidation"}

# Union - toutes les compétences possibles
toutes = classe_guerrier | classe_mage
print(f"Union: {toutes}")

# Intersection - compétences communes
communes = classe_guerrier & classe_mage
print(f"Intersection: {communes}")  # intimidation

# Différence - ce que le guerrier a que le mage n'a pas
unique_guerrier = classe_guerrier - classe_mage
print(f"Unique guerrier: {unique_guerrier}")

# ============================================================
# Différences Tuple vs List vs Set
# ============================================================

print("\n=== Comparaison ===")
print("Tuple: immuable, ordonné, doublons OK -> pour les constantes")
print("List:  mutable, ordonnée, doublons OK -> pour les collections")
print("Set:   mutable, NON ordonné, PAS de doublons -> pour l'unicité")

# ============================================================
# Fin exercice 6 - Les tuples j'aime bien, c'est propre !
# ============================================================
