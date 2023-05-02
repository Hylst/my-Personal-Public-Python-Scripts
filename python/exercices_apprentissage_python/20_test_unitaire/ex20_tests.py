# -*- coding: utf-8 -*-
"""
Exercice 20 : Tests Unitaires
Auteur : Geoffroy Streit
Date : Mai 2023

Tester son code, c'est comme faire une vérification de règles avant la partie !
"""

import unittest

# ============================================================
# Code à tester (fonctions de combat JDR)
# ============================================================

def calculer_modificateur(stat):
    """Calcule le modificateur D&D d'une stat"""
    return (stat - 10) // 2

def calculer_degats(base, modificateur, critique=False):
    """Calcule les dégâts finaux"""
    degats = base + modificateur
    if critique:
        degats *= 2
    return max(0, degats)

def est_reussite(jet, difficulte):
    """Vérifie si un jet est une réussite"""
    return jet >= difficulte

# ============================================================
# Tests unitaires
# ============================================================

class TestModificateur(unittest.TestCase):
    """Tests pour la fonction calculer_modificateur"""
    
    def test_stat_moyenne(self):
        """Stat 10-11 donne modificateur 0"""
        self.assertEqual(calculer_modificateur(10), 0)
        self.assertEqual(calculer_modificateur(11), 0)
    
    def test_stat_haute(self):
        """Stats hautes donnent bonus positif"""
        self.assertEqual(calculer_modificateur(16), 3)
        self.assertEqual(calculer_modificateur(18), 4)
        self.assertEqual(calculer_modificateur(20), 5)
    
    def test_stat_basse(self):
        """Stats basses donnent malus négatif"""
        self.assertEqual(calculer_modificateur(8), -1)
        self.assertEqual(calculer_modificateur(6), -2)


class TestDegats(unittest.TestCase):
    """Tests pour la fonction calculer_degats"""
    
    def test_degats_normaux(self):
        """Dégâts normaux = base + mod"""
        self.assertEqual(calculer_degats(8, 3), 11)
        self.assertEqual(calculer_degats(10, 0), 10)
    
    def test_degats_critiques(self):
        """Dégâts critiques sont doublés"""
        self.assertEqual(calculer_degats(8, 3, True), 22)
    
    def test_degats_minimum_zero(self):
        """Les dégâts ne peuvent pas être négatifs"""
        self.assertEqual(calculer_degats(2, -5), 0)
    
    def test_avec_malus(self):
        """Test avec modificateur négatif"""
        self.assertEqual(calculer_degats(10, -2), 8)


class TestReussite(unittest.TestCase):
    """Tests pour la fonction est_reussite"""
    
    def test_reussite_exacte(self):
        """Égalité = réussite"""
        self.assertTrue(est_reussite(15, 15))
    
    def test_reussite_superieure(self):
        """Jet supérieur = réussite"""
        self.assertTrue(est_reussite(18, 15))
    
    def test_echec(self):
        """Jet inférieur = échec"""
        self.assertFalse(est_reussite(10, 15))


# ============================================================
# Exécution des tests
# ============================================================

if __name__ == "__main__":
    print("🧪 Lancement des tests unitaires\n")
    
    # Exécution avec verbosité
    unittest.main(verbosity=2)
