# -*- coding: utf-8 -*-
"""
Exercice 19 : Appel à une API (requests)
Auteur : Geoffroy Streit
Date : Mai 2023

Bon ça marche, j'ai galéré un peu au début avec les headers...
"""

import requests
import json

# ============================================================
# GET basique - Récupérer des données
# ============================================================

print("=== REQUÊTE GET ===\n")

# API publique de test (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    
    print(f"Status code: {response.status_code}")
    print(f"Headers Content-Type: {response.headers.get('Content-Type')}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nTitre: {data['title']}")
        print(f"Contenu: {data['body'][:100]}...")
    else:
        print(f"Erreur: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"⚠️ Erreur de connexion: {e}")

# ============================================================
# GET avec paramètres
# ============================================================

print("\n=== GET AVEC PARAMÈTRES ===\n")

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1, "_limit": 3}

try:
    response = requests.get(url, params=params, timeout=5)
    posts = response.json()
    
    print(f"Nombre de posts: {len(posts)}")
    for post in posts:
        print(f"  - {post['id']}: {post['title'][:40]}...")
        
except requests.exceptions.RequestException as e:
    print(f"⚠️ Erreur: {e}")

# ============================================================
# POST - Envoyer des données
# ============================================================

print("\n=== REQUÊTE POST ===\n")

url = "https://jsonplaceholder.typicode.com/posts"
nouveau_post = {
    "title": "Mon aventure en Python",
    "body": "Aujourd'hui j'ai appris à utiliser requests !",
    "userId": 42
}

try:
    response = requests.post(
        url,
        json=nouveau_post,  # Envoie en JSON automatiquement
        timeout=5
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 201:  # Created
        resultat = response.json()
        print(f"✅ Post créé avec ID: {resultat['id']}")
        print(f"Contenu: {resultat}")
        
except requests.exceptions.RequestException as e:
    print(f"⚠️ Erreur: {e}")

# ============================================================
# Headers personnalisés
# ============================================================

print("\n=== HEADERS PERSONNALISÉS ===\n")

headers = {
    "User-Agent": "MonScriptPython/1.0",
    "Accept": "application/json"
}

try:
    response = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5
    )
    print(f"Headers envoyés: {response.json()['headers']}")
    
except requests.exceptions.RequestException as e:
    print(f"⚠️ Erreur: {e}")

print("\n✅ Exercice 19 terminé !")
print("Note: toujours utiliser timeout et try/except avec requests !")
