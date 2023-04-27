# -*- coding: utf-8 -*-
"""
Module : utils_jdr.py
Auteur : Geoffroy Streit
Date : Avril 2023

Mon premier module ! Des utilitaires pour le JDR.
"""

import random

def lancer_de(faces=6):
    """Lance un dé avec le nombre de faces spécifié"""
    return random.randint(1, faces)

def lancer_des(nombre, faces=6):
    """Lance plusieurs dés et retourne liste + total"""
    resultats = [lancer_de(faces) for _ in range(nombre)]
    return resultats, sum(resultats)

def modificateur(stat):
    """Calcule le modificateur D&D d'une stat"""
    return (stat - 10) // 2

def jet_caracteristique(stat):
    """Fait un jet de caractéristique (d20 + mod)"""
    mod = modificateur(stat)
    jet = lancer_de(20)
    return jet, mod, jet + mod

# Constantes utiles
CLASSES = ["Guerrier", "Mage", "Voleur", "Clerc", "Paladin"]
RACES = ["Humain", "Elfe", "Nain", "Halfelin", "Demi-orque"]
