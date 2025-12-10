from creation_login import creation_login 

#  FONCTION : Créer un utilisateu
def creation_user():
    print("--- Création utilisateur ---")
    prenom = input("Prénom : ")
    nom = input("Nom : ")

    login = creation_login(prenom, nom)                             # Utilisation de la fonction login

    print("Login généré : ", login)

    # Sélection du rôle
    print("Rôles disponibles : admin / user")
    role = input("Rôle : ").lower()

    if role not in ("admin", "user"):
        print("Rôle invalide.")
        return

    # SITE uniquement pour admin
    if role == "admin" or "SuperAdmin":
        print("Sites disponibles : marseille / rennes / grenoble")
        site = input("Site : ").lower()

        if site not in ("paris", "marseille", "rennes", "grenoble"):
            print("Site invalide.")
            return
    else:
        site = None

#creation_user()                                                        #Pour test fonction