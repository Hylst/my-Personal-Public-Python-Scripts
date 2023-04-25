# -*- coding: utf-8 -*-
"""
Exercice 08 : Fonctions
Auteur : Geoffroy Streit
Date : Avril 2023

Les fonctions, c'est comme les sorts - on les apprend une fois,
on les utilise à volonté !
"""

# ============================================================
# Fonctions de base - Les sorts niveau 1
# ============================================================

def saluer():
    """Fonction sans paramètre - le sort le plus simple"""
    print("🎲 Bienvenue à la table de jeu !")

saluer()

def saluer_joueur(nom):
    """Fonction avec un paramètre"""
    print(f"🎮 Bienvenue, {nom} ! Que les dés te soient favorables !")

saluer_joueur("Geoffroy")
saluer_joueur("Alice")

# ============================================================
# Paramètres et retour - Sorts plus avancés  
# ============================================================

def lancer_de(faces=6):
    """Simule un lancer de dé. Par défaut un d6."""
    import random
    return random.randint(1, faces)

# Utilisation
resultat = lancer_de()
print(f"\nLancer de d6: {resultat}")

resultat_d20 = lancer_de(20)
print(f"Lancer de d20: {resultat_d20}")

def lancer_des(nombre, faces=6):
    """Lance plusieurs dés et retourne la liste + total"""
    import random
    resultats = [random.randint(1, faces) for _ in range(nombre)]
    total = sum(resultats)
    return resultats, total  # Retourne un tuple

des, somme = lancer_des(3, 6)
print(f"\n3d6: {des} = {somme}")

# ============================================================
# Arguments nommés et *args, **kwargs
# ============================================================

def creer_personnage(nom, classe, niveau=1, **stats):
    """Crée un personnage avec des stats flexibles"""
    perso = {
        "nom": nom,
        "classe": classe,
        "niveau": niveau

    }
    perso.update(stats)
    return perso

# Utilisation avec kwargs
heros = creer_personnage(
    "Thorin", 
    "Guerrier", 
    niveau=5,
    force=16,
    constitution=14,
    charisme=12
)
print(f"\nPersonnage créé: {heros}")

def afficher_scores(*scores):
    """Accepte un nombre variable de scores"""
    print(f"Scores reçus: {scores}")
    print(f"Total: {sum(scores)}")

afficher_scores(10, 15, 8, 12)

# ============================================================
# Fonctions de calcul de combat
# ============================================================

def calculer_degats(degats_base, modificateur=0, critique=False):
    """Calcule les dégâts finaux d'une attaque"""
    degats = degats_base + modificateur
    if critique:
        degats *= 2
        print("💥 Coup critique !")
    return max(0, degats)  # Jamais négatif

print(f"\nDégâts normaux: {calculer_degats(10, 3)}")
print(f"Dégâts critiques: {calculer_degats(10, 3, True)}")

def jet_attaque(bonus_attaque, classe_armure):
    """Effectue un jet d'attaque complet"""
    jet = lancer_de(20)
    total = jet + bonus_attaque
    
    if jet == 1:
        return "Échec critique", jet, False
    elif jet == 20:
        return "Réussite critique", jet, True
    elif total >= classe_armure:
        return "Touché", jet, True
    else:
        return "Raté", jet, False

resultat, jet, touche = jet_attaque(5, 15)
print(f"\nJet d'attaque: {jet} -> {resultat}")

# ============================================================
# Scope - Attention aux variables locales/globales
# ============================================================

points_totaux = 0  # Variable globale

def gagner_points(points):
    global points_totaux  # Sans ça, ça crée une variable locale
    points_totaux += points
    print(f"Points gagnés: {points}, Total: {points_totaux}")

gagner_points(10)
gagner_points(25)

# ============================================================
# Fin exercice 8 - Les fonctions c'est vraiment le coeur du code !
# ============================================================
