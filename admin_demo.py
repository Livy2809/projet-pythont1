# init_users.py

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def admin_defaut():
    liste = []

    # --- superadmin ---
    superadmin = {
        "prenom": "Super",
        "nom": "Admin",
        "login": "sa.admin",
        "role": "superadmin",
        "site": "tous",
        "password_hash": hash_password("superadmin"),  # mot de passe simple pour la démo
        "actif": True
    }
    liste.append(superadmin)

    # --- admins locaux---
    sites = ["marseille", "rennes", "grenoble"]

    for site in sites:
        user = {
            "prenom": "Admin",
            "nom": site.capitalize(),
            "login": f"a.{site}",
            "role": "admin",
            "site": site,
            "password_hash": hash_password(site),  # mot de passe = nom du site
            "actif": True
        }
        liste.append(user)

    return liste

from admin_demo import admin_defaut

liste_users = admin_defaut()   # On ajoute les admins à la liste
