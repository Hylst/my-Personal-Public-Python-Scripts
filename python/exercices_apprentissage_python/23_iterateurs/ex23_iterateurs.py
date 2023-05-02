# -*- coding: utf-8 -*-
"""
Exercice 23 : Itérateurs Personnalisés
Auteur : Geoffroy Streit
Date : Juin 2023

Créer ses propres itérateurs, c'est comme écrire ses propres règles !
"""

# ============================================================
# Classe Itérateur simple
# ============================================================

class CompteurTours:
    """Itérateur qui compte les tours de jeu"""
    
    def __init__(self, max_tours):
        self.max_tours = max_tours
        self.tour_actuel = 0
    
    def __iter__(self):
        """Retourne l'itérateur lui-même"""
        return self
    
    def __next__(self):
        """Retourne le prochain élément"""
        if self.tour_actuel < self.max_tours:
            self.tour_actuel += 1
            return f"Tour {self.tour_actuel}"
        else:
            raise StopIteration

print("=== ITÉRATEUR COMPTEUR ===\n")
for tour in CompteurTours(5):
    print(f"  {tour}")

# ============================================================
# Itérateur sur collection custom
# ============================================================

class Inventaire:
    """Collection d'objets avec itération"""
    
    def __init__(self):
        self.objets = []
    
    def ajouter(self, objet):
        self.objets.append(objet)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.objets):
            objet = self.objets[self.index]
            self.index += 1
            return objet
        raise StopIteration
    
    def __len__(self):
        return len(self.objets)

print("\n=== ITÉRATEUR INVENTAIRE ===\n")
inv = Inventaire()
inv.ajouter("Épée +1")
inv.ajouter("Bouclier")
inv.ajouter("Potion de soin")

print(f"Inventaire ({len(inv)} objets):")
for objet in inv:
    print(f"  📦 {objet}")

# ============================================================
# Itérateur avec logique métier
# ============================================================

class ParcoursDonjons:
    """Parcours les salles d'un donjon avec des événements"""
    
    def __init__(self, salles):
        self.salles = salles
        self.position = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.position += 1
        if self.position >= len(self.salles):
            raise StopIteration
        
        salle = self.salles[self.position]
        # Logique métier
        if "boss" in salle.lower():
            return f"⚔️ BOSS: {salle}"
        elif "tresor" in salle.lower():
            return f"💎 TRÉSOR: {salle}"
        elif "piege" in salle.lower():
            return f"💀 PIÈGE: {salle}"
        else:
            return f"🚪 Salle: {salle}"

print("\n=== PARCOURS DONJON ===\n")
donjon = [
    "Entrée sombre",
    "Couloir piégé", 
    "Salle aux trésors",
    "Antichambre",
    "Salle du Boss final"
]

for salle in ParcoursDonjons(donjon):
    print(f"  {salle}")

# ============================================================
# Différence iter() et __iter__
# ============================================================

print("\n=== PROTOCOLE ITÉRATEUR ===\n")
print("Pour être itérable, un objet doit implémenter:")
print("  __iter__() -> retourne l'itérateur")
print("  __next__() -> retourne l'élément suivant")
print("  StopIteration -> signale la fin")

print("\n✅ Exercice 23 terminé !")
