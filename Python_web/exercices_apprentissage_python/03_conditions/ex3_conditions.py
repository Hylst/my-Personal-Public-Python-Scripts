# -*- coding: utf-8 -*-
"""
Exercice 03 : Conditions if/elif/else
Auteur : Geoffroy Streit
Date : Avril 2023

Le fameux arbre de décisions, comme dans un livre dont vous êtes le héros !
"""

# ============================================================
# Conditions simples - Le jet de dé du destin
# ============================================================

import random

# Simulation d'un jet de d20
jet_d20 = random.randint(1, 20)
print(f"🎲 Jet de d20: {jet_d20}")

# Résultat du jet
if jet_d20 == 1:
    print("💀 Échec critique ! Tu trébuches sur tes lacets...")
elif jet_d20 == 20:
    print("⭐ Réussite critique ! Le dragon s'incline devant toi !")
elif jet_d20 >= 15:
    print("✅ Belle réussite !")
elif jet_d20 >= 10:
    print("😐 Réussite de justesse...")
else:
    print("❌ Échec. Le gobelin ricane.")

# ============================================================
# Conditions multiples - Système de combat basique
# ============================================================

pv_joueur = 75
pv_max = 100
a_potion = True

print(f"\n--- État du personnage ---")
print(f"PV: {pv_joueur}/{pv_max}")

# Vérification de l'état de santé
if pv_joueur <= 0:
    print("Game Over... Tu aurais dû boire cette potion.")
elif pv_joueur < 25:
    print("⚠️ Attention, tu es gravement blessé !")
    if a_potion:
        print("💊 Tu as une potion, utilise-la vite !")
    else:
        print("😱 Et tu n'as pas de potion... Fuis !")
elif pv_joueur < 50:
    print("🩹 Tu as pris quelques coups, reste prudent.")
else:
    print("💪 Tu es en pleine forme !")

# ============================================================
# Opérateurs logiques - and, or, not
# ============================================================

est_mage = True
a_mana = False
niveau = 12

print(f"\n--- Vérification de capacité ---")

# and - les deux conditions doivent être vraies
if est_mage and a_mana:
    print("🔥 Tu peux lancer une boule de feu !")
elif est_mage and not a_mana:
    print("😓 Tu es mage mais t'as plus de mana... Utilise ton bâton.")

# or - une des conditions suffit
if niveau >= 10 or est_mage:
    print("🏰 Tu peux entrer dans la tour des arcanes")

# Petite erreur que j'ai faite au début : 
# if niveau = 10:  # FAUX ! C'est == pour comparer, pas =
# J'ai mis 10 minutes à trouver pourquoi ça marchait pas... 😅

# ============================================================
# Fin exercice 3 - Les conditions c'est la base !
# ============================================================
