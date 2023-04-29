# -*- coding: utf-8 -*-
"""
Exercice 18 : Fichiers JSON
Auteur : Geoffroy Streit
Date : Mai 2023

JSON, c'est comme le format universel des fiches de perso !
"""

import json
import os

# ============================================================
# Écriture JSON
# ============================================================

print("=== ÉCRITURE JSON ===\n")

personnage = {
    "nom": "Thorin",
    "classe": "Guerrier",
    "niveau": 8,
    "stats": {
        "force": 18,
        "dexterite": 12,
        "constitution": 16,
        "intelligence": 10,
        "sagesse": 11,
        "charisme": 14
    },
    "inventaire": ["Hache +2", "Armure de plates", "Potion de soin x3"],
    "or": 1250,
    "actif": True
}

# Écriture dans un fichier
with open("personnage.json", "w", encoding="utf-8") as f:
    json.dump(personnage, f, ensure_ascii=False, indent=2)

print("Fichier personnage.json créé !")

# JSON vers string
json_str = json.dumps(personnage, ensure_ascii=False, indent=2)
print(f"\nJSON formaté:\n{json_str}")

# ============================================================
# Lecture JSON
# ============================================================

print("\n=== LECTURE JSON ===\n")

with open("personnage.json", "r", encoding="utf-8") as f:
    perso_charge = json.load(f)

print(f"Nom: {perso_charge['nom']}")
print(f"Classe: {perso_charge['classe']}")
print(f"Force: {perso_charge['stats']['force']}")
print(f"Inventaire: {perso_charge['inventaire']}")

# String vers dict
json_exemple = '{"nom": "Gandalf", "niveau": 20}'
mage = json.loads(json_exemple)
print(f"\nDepuis string: {mage}")

# ============================================================
# Cas pratique - Sauvegarde de partie
# ============================================================

print("\n=== SAUVEGARDE DE PARTIE ===\n")

sauvegarde = {
    "version": "1.0",
    "date_sauvegarde": "2023-05-15",
    "joueur": "Geoffroy",
    "campagne": "La Malédiction de Strahd",
    "session": 12,
    "personnages": [
        {"nom": "Thorin", "pv": 45, "position": [5, 3]},
        {"nom": "Elara", "pv": 28, "position": [5, 4]},
        {"nom": "Bilbo", "pv": 22, "position": [6, 3]}
    ],
    "quetes_actives": ["Trouver le Soleil Sacré", "Vaincre Strahd"],
    "temps_de_jeu_heures": 48.5
}

# Sauvegarder
with open("sauvegarde.json", "w", encoding="utf-8") as f:
    json.dump(sauvegarde, f, ensure_ascii=False, indent=2)

# Recharger et afficher
with open("sauvegarde.json", "r", encoding="utf-8") as f:
    save = json.load(f)
    print(f"Campagne: {save['campagne']}")
    print(f"Session: {save['session']}")
    print(f"Personnages:")
    for p in save['personnages']:
        print(f"  - {p['nom']}: {p['pv']} PV")

# Nettoyage
os.remove("personnage.json")
os.remove("sauvegarde.json")

print("\n✅ Exercice 18 terminé !")
