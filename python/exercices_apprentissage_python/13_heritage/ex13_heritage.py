# -*- coding: utf-8 -*-
"""
Exercice 13 : Héritage
Auteur : Geoffroy Streit
Date : Mai 2023

L'héritage, c'est comme les classes de prestige en D&D !
"""

import random

# ============================================================
# Classe parente
# ============================================================

class Personnage:
    """Classe de base pour tous les personnages"""
    
    def __init__(self, nom, niveau=1):
        self.nom = nom
        self.niveau = niveau
        self.pv_max = 10 + niveau * 5
        self.pv = self.pv_max
    
    def attaquer(self):
        degats = random.randint(1, 6)
        return degats
    
    def __str__(self):
        return f"{self.nom} (Niv.{self.niveau})"


# ============================================================
# Classes enfants - Spécialisations
# ============================================================

class Guerrier(Personnage):
    """Le bourrin de l'équipe - Override du calcul de PV"""
    
    def __init__(self, nom, niveau=1):
        super().__init__(nom, niveau)
        # Le guerrier a plus de PV !
        self.pv_max = 15 + niveau * 8
        self.pv = self.pv_max
        self.style_combat = "offensif"
    
    def attaquer(self):
        # Override - le guerrier tape plus fort !
        degats = random.randint(2, 10) + self.niveau
        print(f"⚔️ {self.nom} frappe avec rage !")
        return degats
    
    def cri_de_guerre(self):
        """Capacité unique du guerrier"""
        print(f"🗣️ {self.nom}: 'POUR LA GLOIRE !'")
        return True


class Mage(Personnage):
    """Le cerveau de l'équipe"""
    
    def __init__(self, nom, niveau=1):
        super().__init__(nom, niveau)
        # Moins de PV
        self.pv_max = 8 + niveau * 3
        self.pv = self.pv_max
        # Mais du mana !
        self.mana_max = 10 + niveau * 5
        self.mana = self.mana_max
    
    def attaquer(self):
        degats = random.randint(1, 4)
        print(f"🏑 {self.nom} frappe mollement avec son bâton...")
        return degats
    
    def boule_de_feu(self):
        """Sort de zone - consomme du mana"""
        cout = 5
        if self.mana >= cout:
            self.mana -= cout
            degats = random.randint(8, 16) + self.niveau * 2
            print(f"🔥 {self.nom} lance une boule de feu ! ({self.mana}/{self.mana_max} mana)")
            return degats
        else:
            print(f"😓 {self.nom} n'a plus assez de mana !")
            return 0


class Voleur(Personnage):
    """Le fourbe de l'équipe"""
    
    def __init__(self, nom, niveau=1):
        super().__init__(nom, niveau)
        self.or_vole = 0
    
    def attaquer(self):
        # Attaque sournoise - chance de coup critique
        if random.random() < 0.3:  # 30% de critique
            degats = random.randint(4, 12) * 2
            print(f"🗡️ {self.nom} attaque dans le dos ! CRITIQUE !")
        else:
            degats = random.randint(2, 8)
            print(f"🗡️ {self.nom} attaque furtivement")
        return degats
    
    def voler(self, cible):
        """Tente de voler la cible"""
        if random.random() < 0.5:
            butin = random.randint(5, 20)
            self.or_vole += butin
            print(f"💰 {self.nom} vole {butin} pièces d'or à {cible} !")
            return butin
        else:
            print(f"🚫 {self.nom} se fait repérer !")
            return 0


# ============================================================
# Test des classes
# ============================================================

print("=== CRÉATION DE L'ÉQUIPE ===\n")

equipe = [
    Guerrier("Thorin", 5),
    Mage("Gandalf", 6),
    Voleur("Bilbo", 4)
]

for membre in equipe:
    print(f"{membre} - {membre.pv} PV")

print("\n=== ACTIONS SPÉCIALES ===\n")

equipe[0].cri_de_guerre()
print(f"Boule de feu: {equipe[1].boule_de_feu()} dégâts")
equipe[2].voler("un marchand")

print("\n=== COMBAT ===\n")
for membre in equipe:
    degats = membre.attaquer()
    print(f"  -> {degats} dégâts\n")

print("✅ Exercice 13 terminé !")
