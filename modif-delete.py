from main import liste_users  # récup liste des users

# Modifier ou supprimer le login
login = input("Entrez le login du user : ")

print("Que voulez-vous faire ?")
print("1 - Modifier le user")
print("2 - Supprimer le user")
print("3 - Quitter")

choix = input("Votre choix : ")

def delete_login(login, choix):

    if choix == "1":                                      # Modifier le user
        # On cherche le user correspondant
        for user in liste_users:
            if user["login"] == login:
                nouveau = input("Nouveau login : ")
                user["login"] = nouveau
                print("Login modifié :", nouveau)
                return user

        print("Utilisateur introuvable.")

    elif choix == "2":                                    # Supprimer le user
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

    return login
