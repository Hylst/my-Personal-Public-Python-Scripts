# -*- coding: utf-8 -*-
"""
Exercice 02 : Types et Cast
Auteur : Geoffroy Streit
Date : Avril 2023

On passe au niveau 2 ! Comme quand on upgrade son perso...
"""

# ============================================================
# Les types de données - comme les classes de personnages
# ============================================================

# int - Les points de vie, ça se compte pas en décimales !
pv_max = 100
niveau = 5
print(f"Type de pv_max: {type(pv_max)}")  # <class 'int'>

# float - Pour les calculs de dégâts critiques, faut de la précision
multiplicateur_critique = 1.75
degats_base = 25
degats_crit = degats_base * multiplicateur_critique
print(f"Dégâts critiques: {degats_crit}")

# str - Le nom du héros, évidemment
nom_perso = "Gandalf le Gris"
print(f"Notre héros: {nom_perso}")

# bool - Est-ce qu'on a réussi le jet de sauvegarde ?
jet_reussi = True
est_mort = False
print(f"Jet réussi: {jet_reussi}")

# ============================================================
# Les conversions (cast) - Transformation de classe !
# ============================================================

# str vers int - quand on lit les stats depuis une fiche
niveau_str = "42"
niveau_int = int(niveau_str)
print(f"\nNiveau converti: {niveau_int + 1}")  # On peu faire des maths maintenant

# int vers str - pour l'affichage
score = 1337
message = "Score final: " + str(score)
print(message)

# float vers int - on arrondis les dégâts (vers le bas, pas de pitié)
degats_precis = 45.7
degats_final = int(degats_precis)
print(f"Dégâts finaux: {degats_final}")  # 45, pas d'arrondi

# str vers float
prix_potion = "9.99"
prix = float(prix_potion)
print(f"Prix de la potion: {prix} pièces d'or")

# Attention aux erreurs de cast !
# int("quarante-deux")  # ça, ça crash comme un nat 1
# Bon à savoir pour plus tard quand on verra les exceptions...

# ============================================================
# Fin exercice 2 - J'ai l'impression de comprendre un truc !
# ============================================================
