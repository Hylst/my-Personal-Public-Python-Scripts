# -*- coding: utf-8 -*-
"""
Exercice 22 : Générateurs (yield)
Auteur : Geoffroy Streit
Date : Juin 2023

Les générateurs, c'est comme un MJ qui improvise au fur et à mesure !
"""

# ============================================================
# Générateur simple
# ============================================================

def generateur_simple():
    """Générateur basique avec yield"""
    yield "Premier"
    yield "Deuxième"
    yield "Troisième"

print("=== GÉNÉRATEUR SIMPLE ===\n")
gen = generateur_simple()
print(f"Type: {type(gen)}")
print(f"Next: {next(gen)}")
print(f"Next: {next(gen)}")
print(f"Next: {next(gen)}")

# ============================================================
# Générateur vs Liste
# ============================================================

def generer_jets_de(n, faces=20):
    """Génère n jets de dés - version générateur"""
    import random
    for _ in range(n):
        yield random.randint(1, faces)

def liste_jets_de(n, faces=20):
    """Génère n jets de dés - version liste"""
    import random
    return [random.randint(1, faces) for _ in range(n)]

print("\n=== GÉNÉRATEUR VS LISTE ===\n")

# Avec générateur - mémoire efficace
print("Jets (générateur):")
for jet in generer_jets_de(5):
    print(f"  🎲 {jet}")

# Avec liste - crée tout en mémoire
jets = liste_jets_de(5)
print(f"\nJets (liste): {jets}")

# ============================================================
# Générateur infini
# ============================================================

def generateur_tours():
    """Générateur infini de tours de combat"""
    tour = 1
    while True:
        yield f"Tour {tour}"
        tour += 1

print("\n=== GÉNÉRATEUR INFINI ===\n")
tours = generateur_tours()
for _ in range(5):
    print(next(tours))
print("... (peut continuer à l'infini)")

# ============================================================
# Expression génératrice
# ============================================================

print("\n=== EXPRESSION GÉNÉRATRICE ===\n")

# Comme une list comprehension mais avec ()
carres_gen = (x**2 for x in range(1, 6))
print(f"Type: {type(carres_gen)}")
print(f"Valeurs: {list(carres_gen)}")

# Usage pratique - somme sans créer de liste
somme = sum(x**2 for x in range(1, 1001))
print(f"Somme des carrés 1-1000: {somme}")

# ============================================================
# Générateur avec état
# ============================================================

def initiative():
    """Simule un ordre d'initiative en combat"""
    import random
    combattants = ["Guerrier", "Mage", "Voleur", "Gobelin", "Orc"]
    random.shuffle(combattants)
    for rang, combattant in enumerate(combattants, 1):
        yield rang, combattant

print("\n=== ORDRE D'INITIATIVE ===\n")
for rang, nom in initiative():
    print(f"  {rang}. {nom}")

print("\n✅ Exercice 22 terminé !")
