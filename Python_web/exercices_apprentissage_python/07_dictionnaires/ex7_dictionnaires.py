# -*- coding: utf-8 -*-
"""
Exercice 07 : Dictionnaires
Auteur : Geoffroy Streit  
Date : Avril 2023

Le dictionnaire, c'est la fiche de perso version Python !
CRUD = Create Read Update Delete - les bases de la gestion de données
"""

# ============================================================
# CREATE - Création de dictionnaires
# ============================================================

print("=== CREATE ===\n")

# Méthode classique
personnage = {
    "nom": "Thorin",
    "classe": "Guerrier",
    "niveau": 5,
    "pv": 45,
    "force": 16,
    "or": 150
}
print(f"Personnage créé: {personnage}")

# Dictionnaire vide + ajouts
inventaire = {}
inventaire["arme"] = "Hache naine"
inventaire["armure"] = "Cotte de mailles"
inventaire["potions"] = 3
print(f"Inventaire: {inventaire}")

# Avec dict()
stats = dict(force=16, dex=12, con=14, intel=8, sag=10, cha=14)
print(f"Stats: {stats}")

# ============================================================
# READ - Lecture des données
# ============================================================

print("\n=== READ ===\n")

# Accès direct
print(f"Nom: {personnage['nom']}")
print(f"Niveau: {personnage['niveau']}")

# Avec get() - plus sûr, retourne None si clé absente
print(f"Classe: {personnage.get('classe')}")
print(f"Magie (absente): {personnage.get('magie', 'Aucune')}")  # Valeur par défaut

# Toutes les clés, valeurs, items
print(f"\nClés: {list(personnage.keys())}")
print(f"Valeurs: {list(personnage.values())}")

# Parcours
print("\nFiche de personnage:")
for cle, valeur in personnage.items():
    print(f"  {cle}: {valeur}")

# ============================================================
# UPDATE - Mise à jour
# ============================================================

print("\n=== UPDATE ===\n")

# Modification simple
personnage["pv"] = 50
personnage["niveau"] = 6
print(f"Après level up: niveau={personnage['niveau']}, pv={personnage['pv']}")

# Ajout de nouvelle clé
personnage["experience"] = 1500
print(f"XP ajoutée: {personnage['experience']}")

# Update avec un autre dict
bonus = {"or": 200, "reputation": 5}
personnage.update(bonus)
print(f"Après update: or={personnage['or']}, rep={personnage['reputation']}")

# ============================================================
# DELETE - Suppression
# ============================================================

print("\n=== DELETE ===\n")

# pop() - retourne la valeur supprimée
or_depense = personnage.pop("or")
print(f"Or dépensé: {or_depense}")

# del - suppression directe
del personnage["reputation"]
print(f"Réputation supprimée")

# clear() - vide tout (mais garde le dict)
inventaire_temp = {"clé": "rouillée", "pierre": "bizarre"}
inventaire_temp.clear()
print(f"Inventaire temp vidé: {inventaire_temp}")

# ============================================================
# Cas pratique - Gestion d'équipe
# ============================================================

print("\n=== Cas pratique: Équipe ===\n")

equipe = {
    "guerrier": {"nom": "Thorin", "pv": 50, "arme": "hache"},
    "mage": {"nom": "Gandalf", "pv": 25, "arme": "bâton"},
    "voleur": {"nom": "Bilbo", "pv": 30, "arme": "dague"}
}

# Accès imbriqué
print(f"Le mage s'appelle: {equipe['mage']['nom']}")
print(f"PV du voleur: {equipe['voleur']['pv']}")

# Le guerrier prend des dégâts
equipe["guerrier"]["pv"] -= 10
print(f"PV guerrier après combat: {equipe['guerrier']['pv']}")

# Affichage équipe complète
print("\n📋 Composition de l'équipe:")
for role, perso in equipe.items():
    print(f"  {role.capitalize()}: {perso['nom']} ({perso['pv']} PV)")

# ============================================================
# Fin exercice 7 - Les dicts c'est vraiment puissant !
# ============================================================
