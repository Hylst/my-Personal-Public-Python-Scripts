# -*- coding: utf-8 -*-
"""
Exercice 12 : Classes et Objets
Auteur : Geoffroy Streit
Date : Mai 2023

La POO, c'est comme créer ses propres règles de jeu !
"""

import random

# ============================================================
# Classe de base - Le Personnage
# ============================================================

class Personnage:
    """
    Classe représentant un personnage de JDR.
    Premier essai de POO, soyons indulgents !
    """
    
    def __init__(self, nom, classe, niveau=1):
        """Le constructeur - comme remplir sa fiche de perso"""
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.pv_max = 10 + (niveau * 5)
        self.pv = self.pv_max
        self.experience = 0
        self.inventaire = []
    
    def __str__(self):
        """Représentation textuelle - pour le print()"""
        return f"{self.nom} ({self.classe} niv.{self.niveau})"
    
    def attaquer(self, cible):
        """Attaque une cible"""
        degats = random.randint(1, 6) + self.niveau
        cible.subir_degats(degats)
        print(f"⚔️ {self.nom} attaque {cible.nom} pour {degats} dégâts !")
        return degats
    
    def subir_degats(self, degats):
        """Subit des dégâts"""
        self.pv = max(0, self.pv - degats)
        print(f"💔 {self.nom} subit {degats} dégâts ({self.pv}/{self.pv_max} PV)")
        if self.pv <= 0:
            print(f"💀 {self.nom} est KO !")
    
    def soigner(self, points):
        """Récupère des PV"""
        ancien_pv = self.pv
        self.pv = min(self.pv_max, self.pv + points)
        gain = self.pv - ancien_pv
        print(f"💚 {self.nom} récupère {gain} PV ({self.pv}/{self.pv_max})")
    
    def ajouter_objet(self, objet):
        """Ajoute un objet à l'inventaire"""
        self.inventaire.append(objet)
        print(f"📦 {self.nom} obtient: {objet}")
    
    def afficher_fiche(self):
        """Affiche la fiche du personnage"""
        print(f"\n{'='*40}")
        print(f"📋 FICHE DE PERSONNAGE")
        print(f"{'='*40}")
        print(f"Nom: {self.nom}")
        print(f"Classe: {self.classe}")
        print(f"Niveau: {self.niveau}")
        print(f"PV: {self.pv}/{self.pv_max}")
        print(f"XP: {self.experience}")
        print(f"Inventaire: {self.inventaire if self.inventaire else 'Vide'}")
        print(f"{'='*40}\n")


# ============================================================
# Test de la classe
# ============================================================

print("=== CRÉATION DE PERSONNAGES ===\n")

# Création d'un héros
heros = Personnage("Thorin", "Guerrier", 5)
heros.afficher_fiche()

# Création d'un ennemi
gobelin = Personnage("Gruk le Gobelin", "Monstre", 2)
print(gobelin)

# Combat !
print("\n=== COMBAT ===\n")
heros.attaquer(gobelin)
gobelin.attaquer(heros)
heros.attaquer(gobelin)

# Soin et inventaire
print("\n=== APRÈS COMBAT ===\n")
heros.soigner(10)
heros.ajouter_objet("Dague de gobelin")
heros.ajouter_objet("3 pièces d'or")
heros.afficher_fiche()

print("✅ Exercice 12 terminé - La POO c'est vraiment puissant !")
