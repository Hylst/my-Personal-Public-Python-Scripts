# -*- coding: utf-8 -*-
"""
Exercice 24 : Projet Final Console - Gestionnaire de Quêtes
Auteur : Geoffroy Streit
Date : Juin 2023

Bon j'améliorerai plus tard mais ça tourne ! 
Un mini gestionnaire de quêtes type JDR en console.
"""

import json
import os
from datetime import datetime

# ============================================================
# Classe Quête
# ============================================================

class Quete:
    """Représente une quête dans le journal"""
    
    def __init__(self, titre, description, difficulte="Normal", recompense=100):
        self.id = None
        self.titre = titre
        self.description = description
        self.difficulte = difficulte
        self.recompense = recompense
        self.statut = "Active"
        self.date_creation = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.date_completion = None
    
    def completer(self):
        self.statut = "Complétée"
        self.date_completion = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def abandonner(self):
        self.statut = "Abandonnée"
    
    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "description": self.description,
            "difficulte": self.difficulte,
            "recompense": self.recompense,
            "statut": self.statut,
            "date_creation": self.date_creation,
            "date_completion": self.date_completion
        }
    
    @classmethod
    def from_dict(cls, data):
        quete = cls(data["titre"], data["description"], 
                    data["difficulte"], data["recompense"])
        quete.id = data["id"]
        quete.statut = data["statut"]
        quete.date_creation = data["date_creation"]
        quete.date_completion = data["date_completion"]
        return quete
    
    def __str__(self):
        icone = {"Active": "📜", "Complétée": "✅", "Abandonnée": "❌"}[self.statut]
        return f"{icone} [{self.id}] {self.titre} ({self.difficulte}) - {self.recompense}🪙"


# ============================================================
# Gestionnaire de Quêtes
# ============================================================

class JournalQuetes:
    """Gère la collection de quêtes"""
    
    FICHIER = "quetes.json"
    
    def __init__(self):
        self.quetes = []
        self.prochain_id = 1
        self.charger()
    
    def ajouter(self, quete):
        quete.id = self.prochain_id
        self.prochain_id += 1
        self.quetes.append(quete)
        self.sauvegarder()
        return quete.id
    
    def trouver(self, id_quete):
        for q in self.quetes:
            if q.id == id_quete:
                return q
        return None
    
    def lister(self, statut=None):
        if statut:
            return [q for q in self.quetes if q.statut == statut]
        return self.quetes
    
    def supprimer(self, id_quete):
        quete = self.trouver(id_quete)
        if quete:
            self.quetes.remove(quete)
            self.sauvegarder()
            return True
        return False
    
    def sauvegarder(self):
        data = {
            "prochain_id": self.prochain_id,
            "quetes": [q.to_dict() for q in self.quetes]
        }
        with open(self.FICHIER, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def charger(self):
        if os.path.exists(self.FICHIER):
            with open(self.FICHIER, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.prochain_id = data["prochain_id"]
                self.quetes = [Quete.from_dict(q) for q in data["quetes"]]


# ============================================================
# Interface Console
# ============================================================

def afficher_menu():
    print("\n" + "=" * 50)
    print("🗡️  JOURNAL DE QUÊTES - Menu Principal  🗡️")
    print("=" * 50)
    print("1. Voir toutes les quêtes")
    print("2. Voir quêtes actives")
    print("3. Ajouter une quête")
    print("4. Compléter une quête")
    print("5. Abandonner une quête")
    print("6. Supprimer une quête")
    print("0. Quitter")
    print("-" * 50)

def afficher_quetes(quetes):
    if not quetes:
        print("  Aucune quête trouvée.")
        return
    
    print(f"\n  {'ID':<4} {'Titre':<25} {'Diff.':<10} {'Récomp.':<8} {'Statut'}")
    print("  " + "-" * 60)
    for q in quetes:
        print(f"  {q.id:<4} {q.titre[:24]:<25} {q.difficulte:<10} {q.recompense:<8} {q.statut}")

def demo_mode():
    """Mode démo sans input() pour l'exercice"""
    journal = JournalQuetes()
    
    print("\n🎮 MODE DÉMO - Simulation d'utilisation\n")
    
    # Ajouter des quêtes
    q1 = Quete("Tuer le dragon", "Vaincre le dragon rouge de la montagne", "Épique", 500)
    q2 = Quete("Livrer le colis", "Apporter le paquet au forgeron", "Facile", 50)
    q3 = Quete("Trouver l'épée légendaire", "Récupérer Excalibur dans la grotte", "Difficile", 300)
    
    for q in [q1, q2, q3]:
        journal.ajouter(q)
        print(f"✅ Quête ajoutée: {q.titre}")
    
    # Afficher
    print("\n📋 Quêtes actives:")
    afficher_quetes(journal.lister("Active"))
    
    # Compléter une quête
    quete = journal.trouver(2)
    if quete:
        quete.completer()
        journal.sauvegarder()
        print(f"\n🎉 Quête '{quete.titre}' complétée ! +{quete.recompense}🪙")
    
    # Afficher tout
    print("\n📋 Toutes les quêtes:")
    afficher_quetes(journal.lister())
    
    # Nettoyage fichier de démo
    if os.path.exists(JournalQuetes.FICHIER):
        os.remove(JournalQuetes.FICHIER)
    
    print("\n✅ Démo terminée !")

# ============================================================
# Point d'entrée
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("🎲 PROJET FINAL : Gestionnaire de Quêtes")
    print("=" * 50)
    print("\nCréateur: Geoffroy Streit")
    print("Version: 1.0")
    print("\nCe projet utilise:")
    print("  - Classes et POO")
    print("  - Fichiers JSON pour la persistance")
    print("  - Gestion de dates")
    print("  - Interface console")
    
    demo_mode()
    
    print("\n" + "=" * 50)
    print("🏆 Parcours d'apprentissage Python terminé !")
    print("=" * 50)
