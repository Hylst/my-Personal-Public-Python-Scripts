# -*- coding: utf-8 -*-
"""
Exercice 01 : Print & Variables
Auteur : Geoffroy Streit
Date : Avril 2023

Premiers pas en Python ! Comme un jet de dés, on ne sait jamais 
ce qui va sortir... Soyons indulgents, c'est mon premier script :')
"""

# ============================================================
# Bon allez, on lance les dés de l'aventure Python !
# ============================================================

# Ma première variable - comme choisir son personnage au début d'une partie
nom = "Geoffroy"
age = 45
passion = "jeux de société"

# Affichage basique - le fameux print, notre première incantation magique
print("=== Bienvenue dans mon aventure Python ===")
print("Je m'appelle", nom)
print("J'ai", age, "ans")

# Les f-strings, c'est comme avoir un dé pipé - ça marche toujours mieux !
print(f"Ma passion : {passion}")

# Petit calcul, histoire de montrer qu'on sait compter nos points de vie
points_de_vie = 100
degats = 15
points_restants = points_de_vie - degats

print(f"\nAprès une attaque de gobelin : {points_restants} PV restants")

# Variables multiples sur une ligne - la technique du maître de jeu
force, intelligence, charisme = 14, 16, 12
print(f"\nMes stats de perso D&D : FOR {force}, INT {intelligence}, CHA {charisme}")

# Ok bon, j'espère que ça marche... Sinon je retourne faire du HTML :')
# Note pour moi-même : ne pas oublier les parenthèses du print() en Python 3

# ============================================================
# Fin de l'exercice 1 - Niveau : Apprenti aventurier
# ============================================================
