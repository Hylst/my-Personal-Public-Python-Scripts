# -*- coding: utf-8 -*-
"""
Exercice 09 : Modules et Imports
Auteur : Geoffroy Streit
Date : Avril 2023

Organiser son code, c'est comme ranger sa collection de jeux !
"""

# ============================================================
# Import de notre module personnalisé
# ============================================================

import utils_jdr

print("=== Test de notre module utils_jdr ===\n")

# Utilisation des fonctions
resultat = utils_jdr.lancer_de(20)
print(f"Jet de d20: {resultat}")

des, total = utils_jdr.lancer_des(4, 6)
print(f"4d6: {des} = {total}")

mod = utils_jdr.modificateur(16)
print(f"Modificateur pour stat 16: +{mod}")

# Accès aux constantes
print(f"\nClasses disponibles: {utils_jdr.CLASSES}")

# ============================================================
# Import avec alias et from
# ============================================================

from utils_jdr import lancer_de, lancer_des
from utils_jdr import RACES as races_jouables

print("\n=== Imports directs ===")
print(f"d12: {lancer_de(12)}")
print(f"Races: {races_jouables}")

# ============================================================
# Modules standards Python
# ============================================================

import random
import math
from datetime import datetime

print("\n=== Modules standards ===")
print(f"Random 1-100: {random.randint(1, 100)}")
print(f"Racine de 144: {math.sqrt(144)}")
print(f"Date actuelle: {datetime.now().strftime('%d/%m/%Y')}")

# ============================================================
# Fin exercice 09 - Les modules c'est vraiment pratique !
# ============================================================
