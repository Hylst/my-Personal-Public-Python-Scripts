# -*- coding: utf-8 -*-
"""
Exercice 04 : Boucles for et while
Auteur : Geoffroy Streit
Date : Avril 2023

Les boucles, c'est comme les tours de jeu - ça continue jusqu'à ce que...
"""

# ============================================================
# Boucle for - Le tour de table
# ============================================================

print("=== Boucle for basique ===")
joueurs = ["Alice", "Bob", "Charlie", "Diana"]

print("C'est le tour de :")
for joueur in joueurs:
    print(f"  🎮 {joueur}")

# Avec range - lancer 5 dés
print("\n=== Lancer de 5 dés ===")
import random

for i in range(5):
    resultat = random.randint(1, 6)
    print(f"Dé {i+1}: {resultat}")

# Range avec start et end
print("\n=== Niveaux 5 à 10 ===")
for niveau in range(5, 11):  # 11 car la borne sup est exclue (j'oublie toujours ça)
    print(f"Niveau {niveau} débloqué !")

# ============================================================
# Boucle while - Tant que le dragon vit...
# ============================================================

print("\n=== Combat contre le dragon ===")
pv_dragon = 50
tour = 0

while pv_dragon > 0:
    tour += 1
    degats = random.randint(8, 15)
    pv_dragon -= degats
    print(f"Tour {tour}: Tu infliges {degats} dégâts ! (Dragon: {max(0, pv_dragon)} PV)")

print(f"🏆 Victoire en {tour} tours !")

# ============================================================
# break et continue - Les jokers du jeu
# ============================================================

print("\n=== Recherche d'un trésor ===")
coffres = ["vide", "piège", "vide", "TRESOR", "vide", "piège"]

for i, coffre in enumerate(coffres):
    print(f"Ouverture du coffre {i+1}...")
    
    if coffre == "piège":
        print("  💥 Piège ! Tu perds 5 PV mais tu continues.")
        continue  # On passe au coffre suivant
    
    if coffre == "TRESOR":
        print("  💎 TRÉSOR TROUVÉ ! Tu arrêtes de chercher.")
        break  # On sort de la boucle
    
    print("  📦 Coffre vide...")

# ============================================================
# Erreur classique que j'ai faite
# ============================================================

# Boucle infinie oubliée - J'ai du faire Ctrl+C pour arrêter !
# i = 0
# while i < 10:
#     print(i)
#     # oups, j'ai oublié i += 1 ... ça tournait à l'infini 😅

# La version corrigée :
print("\n=== Compteur correct ===")
i = 0
while i < 5:
    print(f"Compteur: {i}")
    i += 1  # NE PAS OUBLIER !!!

# ============================================================
# Fin exercice 4 - Les boucles c'est hypnotisant
# ============================================================
