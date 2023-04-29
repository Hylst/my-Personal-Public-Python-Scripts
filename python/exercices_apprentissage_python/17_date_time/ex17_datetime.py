# -*- coding: utf-8 -*-
"""
Exercice 17 : Dates et Heures
Auteur : Geoffroy Streit
Date : Mai 2023

Le temps passe vite en campagne... faut le tracker !
"""

from datetime import datetime, date, time, timedelta

# ============================================================
# Date et Heure actuelles
# ============================================================

print("=== DATE ET HEURE ACTUELLES ===\n")

maintenant = datetime.now()
print(f"Maintenant: {maintenant}")
print(f"Date seule: {maintenant.date()}")
print(f"Heure seule: {maintenant.time()}")

# Composants
print(f"\nAnnée: {maintenant.year}")
print(f"Mois: {maintenant.month}")
print(f"Jour: {maintenant.day}")
print(f"Heure: {maintenant.hour}h{maintenant.minute}")

# ============================================================
# Création de dates
# ============================================================

print("\n=== CRÉATION DE DATES ===\n")

# Date spécifique
date_campagne = date(2023, 3, 15)
print(f"Début de campagne: {date_campagne}")

# DateTime complet
session_1 = datetime(2023, 3, 15, 20, 0, 0)
print(f"Session 1: {session_1}")

# ============================================================
# Formatage - strftime
# ============================================================

print("\n=== FORMATAGE ===\n")

# Formats courants
print(f"Format FR: {maintenant.strftime('%d/%m/%Y')}")
print(f"Format US: {maintenant.strftime('%m/%d/%Y')}")
print(f"Format ISO: {maintenant.strftime('%Y-%m-%d')}")
print(f"Complet: {maintenant.strftime('%A %d %B %Y à %Hh%M')}")

# Format personnalisé
format_jdr = maintenant.strftime("Session du %d/%m/%Y - %Hh%M")
print(f"Format JDR: {format_jdr}")

# ============================================================
# Parsing - strptime
# ============================================================

print("\n=== PARSING ===\n")

date_str = "25/12/2023 20:00"
date_parsed = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
print(f"String: '{date_str}'")
print(f"Parsé: {date_parsed}")

# ============================================================
# Calculs avec timedelta
# ============================================================

print("\n=== CALCULS TEMPORELS ===\n")

# Prochaine session dans 7 jours
prochaine = maintenant + timedelta(days=7)
print(f"Prochaine session: {prochaine.strftime('%d/%m/%Y')}")

# Il y a combien de temps ?
debut_campagne = datetime(2023, 4, 1)
duree = maintenant - debut_campagne
print(f"Campagne en cours depuis: {duree.days} jours")

# Ajouter heures/minutes
fin_session = maintenant + timedelta(hours=4, minutes=30)
print(f"Fin de session estimée: {fin_session.strftime('%Hh%M')}")

# ============================================================
# Comparaisons
# ============================================================

print("\n=== COMPARAISONS ===\n")

date1 = datetime(2023, 6, 1)
date2 = datetime(2023, 12, 1)

if date1 < date2:
    print(f"{date1.strftime('%d/%m')} est avant {date2.strftime('%d/%m')}")

# Vérifier si une date est passée
if session_1 < maintenant:
    print("La session 1 est passée !")

print("\n✅ Exercice 17 terminé !")
