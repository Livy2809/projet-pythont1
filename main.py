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

liste_users = []

#  Créer un user_log
def creation_user():
    print("--- Création user_log ---")
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

    # Exception Superadmin
    if role == "superadmin":
        site = "tous"   # ou une liste ["paris", "marseille" ...]
        print("Le superadmin a été créé.")

    # Admin site
    elif role == "admin":
        print("Sites accessibles : marseille / rennes / grenoble")
        site = input("Site : ").lower()

        if site not in ("marseille", "rennes", "grenoble"):
            print("Site invalide pour un admin local.")
            return
    # User
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
        "password_hash": pwd_hash,                          
        "actif": True                                               # Compte actif par défaut
    }

    liste_users.append(user)                                     #Ajout de la variable user à liste

    print("Utilisateur créé avec succès !")
    print("Login :", login)
    print("Mot de passe :", pwd)


#  Authentification (3 tentative)
def authentification():
    login = input("Login : ")
    # Recherche user identifié dans la liste
    user_log = next((u for u in liste_users if u["login"] == login), None)          #rechercche le login dans list_users 

    if user_log is None:
        print("Login non trouvé.")
        return None

    # Vérifie si le compte est actif
    if user_log.get("actif") == False:                                              #condition pour vérifier si l'user identifié est actif
        print("Compte bloqué !")
        return None

    tentative = 0
    while tentative < 3:                                                            #on fixe la boucle à 3 essais maximum
        mdp = input("Mot de passe : ")
        mdp_hash = hash_password(mdp)

        if mdp_hash == user_log["password_hash"]:                                   #vérification du mot de passe correct
            print("Connexion réussie ! Bienvenue " + utilisateur["prenom"])
            return user_log  # Retourne l'user logé connecté
        else:
            tentative += 1
            print("Mot de passe incorrect (" + str(tentative) + "/3)")

    user_log["actif"] = False                                                       # Après 3 tentatives, l'élément actif devient inactive
    print("Compte bloqué après 3 tentatives échouées.")
    return None

# Ajout outil de modification ou suppresion

def modif_delete_login(login, choix):

    if choix == "1":  # Modifier le user
        for user in liste_users:
            if user["login"] == login:
                while True:
                    print("--- Modifier utilisateur ---")
                    print("1 - Login")
                    print("2 - Rôle")
                    print("3 - Site")
                    print("0 - Terminer modifications")

                    mod = input("Que voulez-vous modifier ? ")

                    if mod == "1":
                        nouveau = input("Nouveau login : ")
                        user["login"] = nouveau
                        print("Login modifié :", nouveau)

                    elif mod == "2":
                        nouveau = input("Nouveau rôle (superadmin/admin/user) : ").lower()
                        if nouveau in ("superadmin","admin","user"):
                            user["role"] = nouveau
                            print("Rôle modifié :", user["role"])
                        else:
                            print("Rôle invalide.")

                    elif mod == "3":
                        if user["role"] == "admin":
                            nouveau = input("Nouveau site (marseille/rennes/grenoble) : ").lower()
                            if nouveau in ("marseille","rennes","grenoble"):
                                user["site"] = nouveau
                                print("Site modifié :", user["site"])
                            else:
                                print("Site invalide.")
                        else:
                            print("Seuls les admins ont un site.")

                    elif mod == "0":
                        print("Modifications terminées.")
                        break
                    else:
                        print("Choix invalide.")
                return

        print("Utilisateur introuvable.")

    elif choix == "2":  # Supprimer le user
        for user in liste_users:
            if user["login"] == login:
                liste_users.remove(user)
                print("L'utilisateur", login, "a été supprimé.")
                return
        print("Utilisateur introuvable.")

    elif choix == "3":
        print("Fin du programme.")
    else:
        print("Choix invalide.")



# ------------- MENU PRINCIPAL -------------

while True:
    print("--- MENU ---")
    print("1 - Créer un utilisateur")
    print("2 - Afficher la liste des utilisateurs")
    print("3 - Connexion uutilisateur")
    print("4 - Modifier / Supprimer un utilisateur")
    print("0 - Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        creation_user()

    elif choix == "2":
        print("--- LISTE DES UTILISATEURS ---")
        for u in liste_users:
            print(u)

    elif choix == "3":
        authentification()

    elif choix == "4":
        print("1 - Modifier un utilisateur")
        print("2 - Supprimer un utilisateur")
        print("3 - Retour")

        mdf_del_choice = input("Votre choix : ")                        #variable choix modification ou suppression

        if mdf_del_choice in ("1","2"):
            mdf_del_login = input("Entrez le login du user : ")         #variable login à modifier ou supprimer
            modif_delete_login(mdf_del_login, mdf_del_choice)
        else:
            print("Retour menu principal.")

    elif choix == "0":
        print("Fermeture du programme.")
        break

    else:
        print("Choix invalide.")
