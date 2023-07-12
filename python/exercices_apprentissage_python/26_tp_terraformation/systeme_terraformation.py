# -*- coding: utf-8 -*-
"""
TP 26 : Système de Terraformation Planétaire
Auteur : Geoffroy Streit
Date : Juillet 2023

Un truc plus complexe avec plusieurs fichiers qui interagissent.
On gère des planètes, des ressources, et on les transforme.
J'aurais pu faire plus propre mais bon ça marche...
"""

import random
import json
import os
from datetime import datetime, timedelta

# ============================================================
# Constantes - les paramètres du jeu
# ============================================================

TYPES_PLANETES = {
    "rocheuse": {"temp_base": -50, "atmo_base": 0, "eau_base": 0},
    "gazeuse": {"temp_base": -150, "atmo_base": 100, "eau_base": 0},
    "glacée": {"temp_base": -200, "atmo_base": 10, "eau_base": 80},
    "désertique": {"temp_base": 60, "atmo_base": 5, "eau_base": 2}
}

OBJECTIF_HABITABLE = {
    "temperature": (15, 25),  # entre 15 et 25°C
    "atmosphere": (80, 100),  # 80-100% respirable
    "eau": (40, 70)           # 40-70% couverture
}

# ============================================================
# Classe Planète
# ============================================================

class Planete:
    """Represente une planète à terraformer"""
    
    def __init__(self, nom, type_planete):
        if type_planete not in TYPES_PLANETES:
            type_planete = "rocheuse"  # fallback
        
        self.nom = nom
        self.type = type_planete
        base = TYPES_PLANETES[type_planete]
        
        # Paramètres avec un peu de random pour varier
        self.temperature = base["temp_base"] + random.randint(-20, 20)
        self.atmosphere = base["atmo_base"] + random.randint(0, 10)
        self.eau = base["eau_base"] + random.randint(0, 5)
        
        self.tours_ecoules = 0
        self.installations = []
        self.historique = []
    
    def est_habitable(self):
        """Vérifie si la planète est habitable"""
        t_ok = OBJECTIF_HABITABLE["temperature"][0] <= self.temperature <= OBJECTIF_HABITABLE["temperature"][1]
        a_ok = OBJECTIF_HABITABLE["atmosphere"][0] <= self.atmosphere <= OBJECTIF_HABITABLE["atmosphere"][1]
        e_ok = OBJECTIF_HABITABLE["eau"][0] <= self.eau <= OBJECTIF_HABITABLE["eau"][1]
        return t_ok and a_ok and e_ok
    
    def score_habitabilite(self):
        """Calcule un score de 0 à 100"""
        score = 0
        
        # Temperature (40 points max)
        t_min, t_max = OBJECTIF_HABITABLE["temperature"]
        if t_min <= self.temperature <= t_max:
            score += 40
        else:
            # plus c'est loin, moins de points
            dist = min(abs(self.temperature - t_min), abs(self.temperature - t_max))
            score += max(0, 40 - dist)
        
        # Atmosphere (35 points)
        a_min, a_max = OBJECTIF_HABITABLE["atmosphere"]
        if a_min <= self.atmosphere <= a_max:
            score += 35
        else:
            dist = min(abs(self.atmosphere - a_min), abs(self.atmosphere - a_max))
            score += max(0, 35 - dist)
        
        # Eau (25 points)
        e_min, e_max = OBJECTIF_HABITABLE["eau"]
        if e_min <= self.eau <= e_max:
            score += 25
        else:
            dist = min(abs(self.eau - e_min), abs(self.eau - e_max))
            score += max(0, 25 - dist)
        
        return min(100, max(0, score))
    
    def log(self, message):
        """Ajoute au journal"""
        self.historique.append(f"Tour {self.tours_ecoules}: {message}")
    
    def afficher_status(self):
        print(f"\n{'='*50}")
        print(f"🪐 PLANÈTE: {self.nom} ({self.type})")
        print(f"{'='*50}")
        print(f"  🌡️  Température: {self.temperature}°C")
        print(f"  💨 Atmosphère: {self.atmosphere}%")
        print(f"  💧 Eau: {self.eau}%")
        print(f"  📊 Score habitabilité: {self.score_habitabilite()}/100")
        if self.est_habitable():
            print(f"  ✅ PLANÈTE HABITABLE !")
        print(f"  🏗️  Installations: {len(self.installations)}")
        print(f"  ⏱️  Tours: {self.tours_ecoules}")
    
    def to_dict(self):
        return {
            "nom": self.nom,
            "type": self.type,
            "temperature": self.temperature,
            "atmosphere": self.atmosphere,
            "eau": self.eau,
            "tours": self.tours_ecoules,
            "installations": self.installations,
            "historique": self.historique[-10:]  # garder les 10 derniers
        }


# ============================================================
# Installations de terraformation
# ============================================================

class Installation:
    """Base pour les installations"""
    
    def __init__(self, nom, cout_energie):
        self.nom = nom
        self.cout_energie = cout_energie
        self.active = True
    
    def effet(self, planete):
        """À surcharger dans les sous-classes"""
        pass


class RechauffeurAtmospherique(Installation):
    """Augmente la température"""
    
    def __init__(self):
        super().__init__("Réchauffeur Atmosphérique", 10)
    
    def effet(self, planete):
        if self.active:
            gain = random.randint(2, 5)
            planete.temperature += gain
            planete.log(f"Réchauffeur: +{gain}°C")
            return gain
        return 0


class GenerateurAtmosphere(Installation):
    """Améliore l'atmosphère"""
    
    def __init__(self):
        super().__init__("Générateur d'Atmosphère", 15)
    
    def effet(self, planete):
        if self.active:
            gain = random.randint(3, 8)
            planete.atmosphere = min(100, planete.atmosphere + gain)
            planete.log(f"Générateur Atmo: +{gain}%")
            return gain
        return 0


class ForeurGlacier(Installation):
    """Libère l'eau des glaciers"""
    
    def __init__(self):
        super().__init__("Foreur de Glacier", 12)
    
    def effet(self, planete):
        if self.active:
            gain = random.randint(2, 6)
            planete.eau = min(100, planete.eau + gain)
            planete.log(f"Foreur: +{gain}% eau")
            return gain
        return 0


class RefroidisseurPlanétaire(Installation):
    """Diminue la temperature - pour planètes trop chaudes"""
    
    def __init__(self):
        super().__init__("Refroidisseur Planétaire", 10)
    
    def effet(self, planete):
        if self.active:
            reduction = random.randint(2, 5)
            planete.temperature -= reduction
            planete.log(f"Refroidisseur: -{reduction}°C")
            return reduction
        return 0


# ============================================================
# Gestionnaire de Projet
# ============================================================

class ProjetTerraformation:
    """Gère un projet de terraformation complet"""
    
    def __init__(self, planete, budget_energie=100):
        self.planete = planete
        self.energie = budget_energie
        self.energie_par_tour = 20
        self.installations = []
        self.termine = False
    
    def construire(self, installation):
        """Construit une installation"""
        self.installations.append(installation)
        self.planete.installations.append(installation.nom)
        print(f"🏗️ Construction: {installation.nom}")
    
    def executer_tour(self):
        """Exécute un tour de terraformation"""
        self.planete.tours_ecoules += 1
        self.energie += self.energie_par_tour
        
        print(f"\n--- Tour {self.planete.tours_ecoules} ---")
        
        # Exécuter chaque installation
        for inst in self.installations:
            if self.energie >= inst.cout_energie:
                self.energie -= inst.cout_energie
                inst.effet(self.planete)
            else:
                print(f"⚠️ {inst.nom}: Énergie insuffisante")
        
        # Vérifier si terminé
        if self.planete.est_habitable():
            self.termine = True
        
        print(f"⚡ Énergie restante: {self.energie}")
    
    def simulation_auto(self, max_tours=50):
        """Lance une simulation automatique"""
        print("\n" + "=" * 60)
        print("🚀 DÉBUT DE LA TERRAFORMATION")
        print("=" * 60)
        
        self.planete.afficher_status()
        
        while not self.termine and self.planete.tours_ecoules < max_tours:
            self.executer_tour()
            
            # Afficher status tous les 10 tours
            if self.planete.tours_ecoules % 10 == 0:
                self.planete.afficher_status()
        
        print("\n" + "=" * 60)
        if self.termine:
            print("🎉 TERRAFORMATION RÉUSSIE !")
        else:
            print("⏸️ Simulation interrompue (limite de tours)")
        print("=" * 60)
        
        self.planete.afficher_status()
        return self.termine


# ============================================================
# Programme principal
# ============================================================

if __name__ == "__main__":
    print("🌌 SYSTÈME DE TERRAFORMATION PLANÉTAIRE v1.0")
    print("============================================\n")
    
    # Créer une planète
    mars = Planete("Mars II", "rocheuse")
    mars.afficher_status()
    
    # Créer le projet
    projet = ProjetTerraformation(mars, budget_energie=50)
    
    # Construire des installations adaptées
    # Mars est froide et n'a pas d'atmosphère ni d'eau
    projet.construire(RechauffeurAtmospherique())
    projet.construire(RechauffeurAtmospherique())  # 2 pour aller plus vite
    projet.construire(GenerateurAtmosphere())
    projet.construire(ForeurGlacier())
    
    # Lancer la simulation
    succes = projet.simulation_auto(max_tours=30)
    
    # Sauvegarder le résultat
    with open("terraformation_result.json", "w", encoding="utf-8") as f:
        json.dump(mars.to_dict(), f, ensure_ascii=False, indent=2)
    print("\n📁 Résultat sauvegardé dans terraformation_result.json")
    
    # Nettoyage
    if os.path.exists("terraformation_result.json"):
        os.remove("terraformation_result.json")
    
    print("\n✅ TP terminé !")
    # c'est un peu bourrin comme approche mais ça illustre bien le concept
