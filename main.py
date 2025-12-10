

def creation_login(prenom, nom):
    """
    Règle du TP :
    Login = première lettre du prénom + nom (non composé)
    Exemple : Olivia Uba → ouba
    """
    prenom = prenom.strip().lower()
    nom = nom.strip().lower().split()[0]  # nom non composé

    return prenom[0] + nom

def create_user(current_user):
    print("\n--- Création d'un utilisateur ---")

    # 1) Récupération des infos
    prenom = input("Prénom : ").strip()
    nom = input("Nom : ").strip()
    email = input("Email : ").strip()

    # 2) Génération login
    login = creation_login(prenom, nom)

    # Charger users depuis CSV
    users = load_users()

    # Si login existe : ajouter un suffixe
    base_login = login
    i = 1
    while find_user_by_login(users, login):
        login = f"{base_login}{i}"
        i += 1

    print(f"✔ Login généré : {login}")

    # 3) Choix du rôle
    role = input("Rôle (Admin / User) : ").strip().capitalize()

    if role not in ("Admin", "User"):
        print("❌ Rôle invalide.")
        return

    # 4) Choix du site si Admin
    if role == "Admin":
        site = input("Site (Marseille / Rennes / Grenoble) : ").strip().capitalize()

        if site not in ("Marseille", "Rennes", "Grenoble"):
            print("❌ Site invalide.")
            return

        # Un admin ne peut créer que sur son propre site
        if current_user["role"].lower() == "admin" and current_user["site"].lower() != site.lower():
            print("❌ Vous ne pouvez créer des utilisateurs que dans votre site.")
            return
    else:
        site = "Aucun"

    # 5) Génération mot de passe + hash
    password = generate_password(10)
    salt = generate_salt()
    password_hash = hash_password(password, salt)

    # 6) Création de l'utilisateur
    new_user = {
        "login": login,
        "password_hash": password_hash,
        "salt": salt,
        "role": role,
        "site": site,
        "email": email,
        "blocked_until": "",
        "password_changed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # 7) Sauvegarde dans le CSV
    users.append(new_user)
    save_users(users)

    # 8) Résultat
    print("\n✔ Utilisateur créé avec succès !")
    print(f"   Login : {login}")
    print(f"   Mot de passe temporaire : {password}")
    print("   (à changer à la première connexion)")

