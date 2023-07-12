# -*- coding: utf-8 -*-
"""
TP 25 : Simulateur de Flotte Spatiale
Auteur : Geoffroy Streit
Date : Juillet 2023

Bon je change de thème, on passe au SF ! 
Ras le bol des goblins, place aux vaisseaux spatiaux 🚀
"""

import random
from datetime import datetime
import json

# ============================================================
# Classes de vaisseaux
# ============================================================

class Vaisseau:
    """Classe de base pour tous les vaisseaux"""
    
    def __init__(self, nom, type_vaisseau):
        self.nom = nom
        self.type = type_vaisseau
        self.coque = 100
        self.bouclier = 50
        self.energie = 100
        self.position = [0, 0, 0]  # x, y, z dans l'espace
        self.vitesse = 0
        self.actif = True
    
    def deplacer(self, dx, dy, dz):
        """Déplace le vaisseau - consomme de l'énergie"""
        cout = abs(dx) + abs(dy) + abs(dz)
        if self.energie >= cout:
            self.position[0] += dx
            self.position[1] += dy
            self.position[2] += dz
            self.energie -= cout
            return True
        print(f"⚠️ {self.nom}: Energie insuffisante !")
        return False
    
    def subir_degats(self, degats):
        """Gère les dégâts reçus - bouclier puis coque"""
        if self.bouclier > 0:
            if degats <= self.bouclier:
                self.bouclier -= degats
                print(f"🛡️ {self.nom}: Bouclier absorbe {degats} dégâts")
            else:
                reste = degats - self.bouclier
                self.bouclier = 0
                self.coque -= reste
                print(f"💥 {self.nom}: Bouclier détruit ! Coque: -{reste}")
        else:
            self.coque -= degats
            print(f"💥 {self.nom}: Coque touchée ! -{degats}")
        
        if self.coque <= 0:
            self.actif = False
            print(f"💀 {self.nom} DÉTRUIT !")
    
    def reparer(self, points):
        """Répare la coque"""
        self.coque = min(100, self.coque + points)
        print(f"🔧 {self.nom} réparé: {self.coque}/100")
    
    def recharger_bouclier(self):
        """Recharge le bouclier - coute de l'énergie"""
        if self.energie >= 20:
            self.bouclier = min(50, self.bouclier + 25)
            self.energie -= 20
            print(f"🔋 {self.nom}: Bouclier rechargé à {self.bouclier}")
    
    def __str__(self):
        status = "🟢" if self.actif else "💀"
        return f"{status} {self.nom} ({self.type}) - Coque:{self.coque} Bouclier:{self.bouclier}"


class Chasseur(Vaisseau):
    """Petit vaisseau rapide - fait pas beaucoup de dégâts mais esquive bien"""
    
    def __init__(self, nom):
        super().__init__(nom, "Chasseur")
        self.coque = 50  # fragile
        self.bouclier = 20
        self.degats = 15
        self.esquive = 0.4  # 40% d'esquive
    
    def attaquer(self, cible):
        if random.random() < cible.esquive if hasattr(cible, 'esquive') else 0:
            print(f"💨 {cible.nom} esquive l'attaque de {self.nom} !")
            return 0
        degats = random.randint(10, self.degats)
        cible.subir_degats(degats)
        return degats


class Croiseur(Vaisseau):
    """Vaisseau moyen - équilibré"""
    
    def __init__(self, nom):
        super().__init__(nom, "Croiseur")
        self.coque = 150
        self.bouclier = 75
        self.degats = 30
        self.missiles = 4
    
    def attaquer(self, cible):
        degats = random.randint(20, self.degats)
        cible.subir_degats(degats)
        return degats
    
    def tirer_missile(self, cible):
        """Tire un missile - gros dégâts mais limité"""
        if self.missiles > 0:
            self.missiles -= 1
            degats = random.randint(40, 60)
            print(f"🚀 {self.nom} tire un missile sur {cible.nom} !")
            cible.subir_degats(degats)
            print(f"   Missiles restants: {self.missiles}")
            return degats
        print(f"❌ {self.nom}: Plus de missiles !")
        return 0


class Cuirasse(Vaisseau):
    """Gros vaisseau lourd - tank"""
    
    def __init__(self, nom):
        super().__init__(nom, "Cuirassé")
        self.coque = 300
        self.bouclier = 150
        self.degats = 50
        self.tourelles = 3
    
    def attaquer(self, cible):
        total = 0
        for i in range(self.tourelles):
            degats = random.randint(15, 25)
            total += degats
        print(f"💥 {self.nom} tire avec {self.tourelles} tourelles !")
        cible.subir_degats(total)
        return total


# ============================================================
# Gestionnaire de Flotte
# ============================================================

class Flotte:
    """Gère une flotte de vaisseaux"""
    
    def __init__(self, nom_faction):
        self.nom = nom_faction
        self.vaisseaux = []
    
    def ajouter(self, vaisseau):
        self.vaisseaux.append(vaisseau)
        print(f"➕ {vaisseau.nom} rejoint la flotte {self.nom}")
    
    def vaisseaux_actifs(self):
        return [v for v in self.vaisseaux if v.actif]
    
    def afficher_status(self):
        print(f"\n{'='*50}")
        print(f"🚀 FLOTTE: {self.nom}")
        print(f"{'='*50}")
        for v in self.vaisseaux:
            print(f"  {v}")
        actifs = len(self.vaisseaux_actifs())
        print(f"\nVaisseaux actifs: {actifs}/{len(self.vaisseaux)}")
    
    def est_detruite(self):
        return len(self.vaisseaux_actifs()) == 0


# ============================================================
# Simulation de combat
# ============================================================

def simuler_combat(flotte1, flotte2):
    """Simule un combat entre deux flottes"""
    
    print("\n" + "=" * 60)
    print("⚔️  DÉBUT DU COMBAT SPATIAL  ⚔️")
    print(f"{flotte1.nom} VS {flotte2.nom}")
    print("=" * 60)
    
    tour = 0
    while not flotte1.est_detruite() and not flotte2.est_detruite():
        tour += 1
        print(f"\n--- Tour {tour} ---")
        
        # Flotte 1 attaque
        for v in flotte1.vaisseaux_actifs():
            cibles = flotte2.vaisseaux_actifs()
            if cibles:
                cible = random.choice(cibles)
                v.attaquer(cible)
        
        # Flotte 2 riposte
        for v in flotte2.vaisseaux_actifs():
            cibles = flotte1.vaisseaux_actifs()
            if cibles:
                cible = random.choice(cibles)
                v.attaquer(cible)
        
        # Limiter le combat pour la démo
        if tour >= 10:
            print("\n⏸️ Combat interrompu après 10 tours")
            break
    
    print("\n" + "=" * 60)
    if flotte1.est_detruite():
        print(f"🏆 VICTOIRE DE {flotte2.nom} !")
    elif flotte2.est_detruite():
        print(f"🏆 VICTOIRE DE {flotte1.nom} !")
    else:
        print("⚖️ MATCH NUL")
    print("=" * 60)
    
    flotte1.afficher_status()
    flotte2.afficher_status()


# ============================================================
# Demo
# ============================================================

if __name__ == "__main__":
    print("🌌 SIMULATEUR DE FLOTTE SPATIALE v1.0")
    print("=====================================\n")
    
    # Création des flottes
    federation = Flotte("Fédération Terrienne")
    federation.ajouter(Cuirasse("USS Enterprise"))
    federation.ajouter(Croiseur("USS Voyager"))
    federation.ajouter(Chasseur("Alpha-1"))
    federation.ajouter(Chasseur("Alpha-2"))
    
    empire = Flotte("Empire Zorgon")
    empire.ajouter(Cuirasse("Destructeur Suprême"))
    empire.ajouter(Croiseur("Faucon Noir"))
    empire.ajouter(Croiseur("Ombre Stellaire"))
    empire.ajouter(Chasseur("Drone-X1"))
    
    # Affichage initial
    federation.afficher_status()
    empire.afficher_status()
    
    # Combat !
    simuler_combat(federation, empire)
    
    print("\n✅ Simulation terminée !")
    # bon c'est pas parfait mais ça donne une idée
