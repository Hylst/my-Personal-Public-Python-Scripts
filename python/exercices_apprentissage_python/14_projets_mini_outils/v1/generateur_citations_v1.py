# -*- coding: utf-8 -*-
"""
Exercice 14 : Mini-outil V1 - Générateur de Citations
Auteur : Geoffroy Streit
Date : Mai 2023

Première version simple - les citations sont en dur dans le code.
On améliorera ça dans la V2 !
"""

import random

# ============================================================
# V1 - Citations en dur (pas très propre mais ça marche)
# ============================================================

citations_jdr = [
    "Un nat 1, c'est juste un 20 timide.",
    "Le MJ ne ment jamais, il réinterprète la réalité.",
    "Ce n'est pas de la triche, c'est de l'optimisation créative.",
    "Les plans à 20 étapes échouent toujours à l'étape 2.",
    "Si le MJ sourit, c'est mauvais signe. S'il rit, fuyez.",
    "Un voleur n'est pas un escroc, c'est un expert en redistribution.",
    "Les gobelins sont comme les chips, on peut pas en tuer qu'un seul.",
    "L'échec critique du barde a au moins fait fuir les corbeaux.",
    "Le meilleur plan ? Celui qu'on improvise après que le premier ait foiré.",
    "Une épée +1, c'est bien. Une épée +1 volée aux ennemis, c'est mieux."
]

def generer_citation():
    """Génère une citation aléatoire"""
    citation = random.choice(citations_jdr)
    return citation

def afficher_citation():
    """Affiche une citation avec mise en forme"""
    citation = generer_citation()
    separateur = "=" * 60
    print(f"\n{separateur}")
    print(f"📜 CITATION DE MJ DU JOUR")
    print(f"{separateur}")
    print(f"\n  « {citation} »\n")
    print(f"{separateur}\n")

# ============================================================
# Programme principal
# ============================================================

if __name__ == "__main__":
    print("🎲 Générateur de Citations JDR v1.0")
    print("-----------------------------------")
    
    # Affiche 3 citations pour la démo
    for i in range(3):
        afficher_citation()
    
    print("\n✅ V1 terminée - ça marche !")
    print("TODO: charger les citations depuis un fichier externe")
