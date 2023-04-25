# -*- coding: utf-8 -*-
"""
Exercice 10 : Manipulation de fichiers
Auteur : Geoffroy Streit
Date : Mai 2023

Sauvegarder ses parties, c'est important !
"""

# ============================================================
# ÉCRITURE dans un fichier
# ============================================================

print("=== ÉCRITURE ===\n")

# Méthode with - recommandée (ferme auto le fichier)
with open("sauvegarde.txt", "w", encoding="utf-8") as f:
    f.write("=== Sauvegarde de partie ===\n")
    f.write("Joueur: Geoffroy\n")
    f.write("Niveau: 12\n")
    f.write("Or: 1500\n")
    f.write("Position: Taverne du Dragon Rouge\n")

print("Fichier sauvegarde.txt créé !")

# Écriture avec writelines
inventaire = ["Épée longue\n", "Bouclier\n", "3 potions de soin\n"]
with open("inventaire.txt", "w", encoding="utf-8") as f:
    f.write("=== Inventaire ===\n")
    f.writelines(inventaire)

print("Fichier inventaire.txt créé !")

# ============================================================
# LECTURE d'un fichier
# ============================================================

print("\n=== LECTURE ===\n")

# Lire tout le contenu
with open("sauvegarde.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    print("Contenu complet:")
    print(contenu)

# Lire ligne par ligne
print("Lecture ligne par ligne:")
with open("inventaire.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(f"  > {ligne.strip()}")

# Lire dans une liste
with open("inventaire.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()
    print(f"\nNombre de lignes: {len(lignes)}")

# ============================================================
# MODE APPEND - Ajouter sans écraser
# ============================================================

print("\n=== APPEND ===\n")

with open("journal_aventure.txt", "w", encoding="utf-8") as f:
    f.write("Jour 1: L'aventure commence !\n")

# Ajout avec 'a'
with open("journal_aventure.txt", "a", encoding="utf-8") as f:
    f.write("Jour 2: Rencontré un mystérieux étranger...\n")
    f.write("Jour 3: Combat contre des gobelins, victoire !\n")

with open("journal_aventure.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ============================================================
# Vérifier si un fichier existe
# ============================================================

import os

print("=== VÉRIFICATIONS ===\n")

if os.path.exists("sauvegarde.txt"):
    print("✅ La sauvegarde existe !")
    taille = os.path.getsize("sauvegarde.txt")
    print(f"   Taille: {taille} octets")
else:
    print("❌ Pas de sauvegarde trouvée")

# Nettoyage des fichiers de test
# os.remove("sauvegarde.txt")  # Décommentez pour supprimer

print("\n✅ Exercice 10 terminé !")
