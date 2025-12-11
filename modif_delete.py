from main import liste_users  # récup liste des users

# Utilisateur test
liste_users.append({
    "prenom": "Olivia",
    "nom": "Uba",
    "login": "o.uba",
    "role": "user",
    "site": None,
    "Mot de passe ": "hashedpassword123"
})

def delete_login(login, choix):

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


# --- BOUCLE MENU ---
while True:
    print("Que voulez-vous faire ?")
    print("1 - Modifier le user")
    print("2 - Supprimer le user")
    print("3 - Quitter")

    choix = input("Votre choix : ")

    if choix == "3":
        print("Fin du programme.")
        break
    elif choix in ("1", "2"):
        login = input("Entrez le login du user : ")
        delete_login(login, choix)
    else:
        print("Choix invalide, réessayez.")

    # Affichage de la liste pour vérifier
    print("--- LISTE DES UTILISATEURS ---")
    for u in liste_users:
        print(u)
