# -*- coding: utf-8 -*-
"""
Exercice 14 : Mini-outil V2 - Générateur de Citations (amélioré)
Auteur : Geoffroy Streit
Date : Mai 2023

Version améliorée avec fichier externe et plus de fonctionnalités.
Bon j'améliorerai encore plus tard mais ça tourne !
"""

import random
import os

# ============================================================
# Chargement depuis fichier externe
# ============================================================

def charger_citations(fichier="citations.txt"):
    """Charge les citations depuis un fichier texte"""
    chemin = os.path.join(os.path.dirname(__file__), fichier)
    
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            citations = [ligne.strip() for ligne in f if ligne.strip()]
        print(f"📂 {len(citations)} citations chargées depuis {fichier}")
        return citations
    except FileNotFoundError:
        print(f"⚠️ Fichier {fichier} non trouvé, utilisation des citations par défaut")
        return ["Aucune citation disponible - créez le fichier citations.txt !"]

# ============================================================
# Fonctions du générateur
# ============================================================

class GenerateurCitations:
    """Classe pour gérer les citations - c'est plus propre !"""
    
    def __init__(self, fichier="citations.txt"):
        self.citations = charger_citations(fichier)
        self.historique = []
    
    def generer(self, eviter_repetition=True):
        """Génère une citation, évite les répétitions si possible"""
        disponibles = self.citations.copy()
        
        if eviter_repetition and len(self.historique) < len(self.citations):
            disponibles = [c for c in disponibles if c not in self.historique[-5:]]
        
        if not disponibles:
            self.historique = []
            disponibles = self.citations.copy()
        
        citation = random.choice(disponibles)
        self.historique.append(citation)
        return citation
    
    def afficher(self):
        """Affiche une citation formatée"""
        citation = self.generer()
        largeur = min(60, len(citation) + 10)
        sep = "═" * largeur
        
        print(f"\n╔{sep}╗")
        print(f"║ 📜 SAGESSE DE MJ DU JOUR {' ' * (largeur - 26)}║")
        print(f"╠{sep}╣")
        
        # Découpe la citation si trop longue
        mots = citation.split()
        ligne = ""
        for mot in mots:
            if len(ligne) + len(mot) + 1 <= largeur - 4:
                ligne += mot + " "
            else:
                print(f"║  {ligne.ljust(largeur - 3)}║")
                ligne = mot + " "
        if ligne:
            print(f"║  {ligne.ljust(largeur - 3)}║")
        
        print(f"╚{sep}╝\n")
    
    def ajouter_citation(self, nouvelle):
        """Ajoute une nouvelle citation"""
        self.citations.append(nouvelle)
        print(f"✅ Citation ajoutée ! Total: {len(self.citations)}")

# ============================================================
# Programme principal
# ============================================================

if __name__ == "__main__":
    print("🎲 Générateur de Citations JDR v2.0")
    print("=" * 40)
    
    gen = GenerateurCitations()
    
    # Affiche 3 citations
    for _ in range(3):
        gen.afficher()
    
    print(f"\n📊 Historique: {len(gen.historique)} citations générées")
    print("✅ V2 terminée - bien mieux que la V1 !")
