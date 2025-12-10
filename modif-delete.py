#Modifier ou supprimer le login
login = input()

# --- Programme principal ---
print("Que voulez-vous faire ?")
print("1 - Modifier le login")
print("2 - Supprimer le login")
print("3 - Quitter")

choix = input("Votre choix : ")

def mdf_delete_login(login, choix):
    if choix == "1":                                        # Modifier le login
        nouveau = input("Nouveau login : ")
        login = nouveau
        print(f"Login modifié : {login}")

    elif choix == "2":                                      # Supprimer le login
        print("L'utilisateur ", login," a été supprimée.")
        del login

    elif choix == "3":
        print("Fin du programme.")

    else:
        print("Choix invalide.")

    return login
