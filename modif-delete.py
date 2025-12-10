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
                nouveau = input("Nouveau login : ")
                user["login"] = nouveau
                print("Login modifié :", nouveau)
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
