#  FONCTION : Création du login

def creation_login(prenom: str, nom: str):

    prenom = prenom.strip().lower()
    nom = nom.strip().lower()

    # Séparation des prénoms (espace ou tiret)
    separateurs = [" ", "-"]
    for sep in separateurs:
        prenom = prenom.replace(sep, " ")

    liste_prenoms = prenom.split()

    initiales = "".join([pldp[0] for pldp in liste_prenoms])         # Récupération des initiales, pldp = 1ère lettre du prénom

    login = initiales + "." + nom                                   # Construction du login

    return login

#  GÉNÉRATION MOT DE PASSE

import random                                                       # import module sélection aléatoire
import hashlib                                                      # import module de hashage
import string                                                       # import module string

def generate_password(taille=10):                                   # création fonction génération mot de passe selon                          
    char=string.ascii_letters+string.digits+string.punctuation      # présentation normes du mot de passe
                                                                                    # string.ascii_letters
                                                                                    # string.digits
                                                                                    # string.punctuation
    pwd = "".join(random.choice(char) for _ in range(taille))      # sélection de 10 chaîne de caractère aléatoire
    return pwd

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


liste_users = []   # liste d'utilisateurs

#  FONCTION : Créer un utilisateur

def creer_utilisateur():
    print("--- Création utilisateur ---")
    prenom = input("Prénom : ")
    nom = input("Nom : ")

    login = creation_login(prenom, nom)                             # Utilisation de la fonction login

    print("Login généré : ", login)

    # Sélection du rôle
    print("Rôles disponibles : superadmin / admin / user")
    role = input("Rôle : ").lower()

    if role not in ("superadmin", "admin", "user"):
        print("Rôle invalide.")
        return

    # SITE uniquement pour admin
    if role == "admin":
        print("Sites disponibles : marseille / rennes / grenoble")
        site = input("Site : ").lower()

        if site not in ("marseille", "rennes", "grenoble"):
            print("Site invalide.")
            return
    else:
        site = None

    # Initialisation password
    pwd = generate_password()
    pwd_hash = hash_password(pwd)

    # STOCKAGE DANS LA LISTE
    user = {
        "prenom": prenom,
        "nom": nom,
        "login": login,
        "role": role,
        "site": site,
        "Mot de passe ": pwd_hash
    }

    liste_users.append(user)                                      #Ajout de 

    print("✔ Utilisateur créé avec succès !")
    print("Login :", login)
    print("Mot de passe temporaire :", pwd)


# MINI-MENU POUR TESTE

    while True:
        print("--- MENU ---")
        print("1 - Créer un utilisateur")
        print("2 - Afficher la liste des utilisateurs")
        print("0 - Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            creer_utilisateur()

        elif choix == "2":
            print("--- LISTE DES UTILISATEURS ---")
            for u in liste_users:
                print(u)

        elif choix == "0":
            print("Fermeture du programme.")
            break

        else:
            print("Choix invalide.")