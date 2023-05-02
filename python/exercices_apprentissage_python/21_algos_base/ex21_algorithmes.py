# -*- coding: utf-8 -*-
"""
Exercice 21 : Algorithmes de Base
Auteur : Geoffroy Streit
Date : Juin 2023

Les algos classiques, comme les stratégies de combat éprouvées !
"""

# ============================================================
# RECHERCHE - Trouver un élément
# ============================================================

def recherche_lineaire(liste, cible):
    """Recherche séquentielle - O(n)"""
    for i, element in enumerate(liste):
        if element == cible:
            return i
    return -1

def recherche_binaire(liste_triee, cible):
    """Recherche dichotomique - O(log n) - liste doit être triée !"""
    gauche, droite = 0, len(liste_triee) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste_triee[milieu] == cible:
            return milieu
        elif liste_triee[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1

# ============================================================
# TRI - Ordonner les éléments
# ============================================================

def tri_bulle(liste):
    """Tri à bulles - O(n²) - simple mais lent"""
    arr = liste.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def tri_selection(liste):
    """Tri par sélection - O(n²)"""
    arr = liste.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def tri_insertion(liste):
    """Tri par insertion - O(n²) mais efficace sur petites listes"""
    arr = liste.copy()
    for i in range(1, len(arr)):
        cle = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cle:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cle
    return arr

# ============================================================
# Tests
# ============================================================

print("=== TESTS RECHERCHE ===\n")

monstres = ["gobelin", "orc", "dragon", "troll", "squelette"]
print(f"Liste: {monstres}")
print(f"Recherche 'dragon': index {recherche_lineaire(monstres, 'dragon')}")

niveaux = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"\nListe triée: {niveaux}")
print(f"Recherche binaire 11: index {recherche_binaire(niveaux, 11)}")

print("\n=== TESTS TRI ===\n")

degats = [15, 3, 8, 20, 1, 12, 7]
print(f"Original: {degats}")
print(f"Tri bulle: {tri_bulle(degats)}")
print(f"Tri sélection: {tri_selection(degats)}")
print(f"Tri insertion: {tri_insertion(degats)}")

print("\n✅ Exercice 21 terminé !")
