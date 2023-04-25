# -*- coding: utf-8 -*-
"""
Exercice 11 : Gestion des Exceptions
Auteur : Geoffroy Streit
Date : Mai 2023

Parce que même un nat 20 ne protège pas des erreurs de code...
"""

# ============================================================
# Try/Except basique
# ============================================================

print("=== TRY/EXCEPT BASIQUE ===\n")

# Division par zéro
def diviser(a, b):
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("⚠️ Erreur: Division par zéro impossible !")
        return None

print(f"10 / 2 = {diviser(10, 2)}")
print(f"10 / 0 = {diviser(10, 0)}")

# Conversion invalide
def convertir_en_int(valeur):
    try:
        return int(valeur)
    except ValueError:
        print(f"⚠️ '{valeur}' n'est pas un nombre valide !")
        return 0

print(f"\nConversion '42': {convertir_en_int('42')}")
print(f"Conversion 'abc': {convertir_en_int('abc')}")

# ============================================================
# Exceptions multiples
# ============================================================

print("\n=== EXCEPTIONS MULTIPLES ===\n")

def acces_liste(liste, index):
    try:
        return liste[index]
    except IndexError:
        print(f"⚠️ Index {index} hors limites !")
        return None
    except TypeError:
        print("⚠️ L'index doit être un entier !")
        return None

inventaire = ["épée", "bouclier", "potion"]
print(f"Index 0: {acces_liste(inventaire, 0)}")
print(f"Index 10: {acces_liste(inventaire, 10)}")
print(f"Index 'a': {acces_liste(inventaire, 'a')}")

# ============================================================
# Finally - Toujours exécuté
# ============================================================

print("\n=== FINALLY ===\n")

def lire_fichier_safe(nom):
    try:
        f = open(nom, "r")
        contenu = f.read()
        print(f"Lu: {contenu[:50]}...")
        return contenu
    except FileNotFoundError:
        print(f"⚠️ Fichier '{nom}' non trouvé !")
        return None
    finally:
        print("🔒 Nettoyage terminé (finally toujours exécuté)")

lire_fichier_safe("fichier_inexistant.txt")

# ============================================================
# Lever ses propres exceptions
# ============================================================

print("\n=== RAISE ===\n")

def jet_de_caracteristique(valeur):
    if valeur < 1 or valeur > 20:
        raise ValueError(f"Valeur {valeur} invalide ! (1-20 requis)")
    return valeur

try:
    print(f"Jet valide: {jet_de_caracteristique(15)}")
    print(f"Jet invalide: {jet_de_caracteristique(25)}")
except ValueError as e:
    print(f"⚠️ Erreur attrapée: {e}")

# ============================================================
# Cas pratique - Saisie sécurisée
# ============================================================

print("\n=== SAISIE SÉCURISÉE ===\n")

def demander_nombre(message, min_val=1, max_val=100):
    """Simule une saisie avec valeur par défaut pour l'exercice"""
    valeur_test = "42"  # En vrai on utiliserait input()
    try:
        nombre = int(valeur_test)
        if nombre < min_val or nombre > max_val:
            raise ValueError(f"Hors limites ({min_val}-{max_val})")
        return nombre
    except ValueError as e:
        print(f"Erreur: {e}, utilisation valeur par défaut")
        return min_val

resultat = demander_nombre("Entrez un nombre: ", 1, 20)
print(f"Nombre obtenu: {resultat}")

print("\n✅ Exercice 11 terminé - Les exceptions c'est vital !")
