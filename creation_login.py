#Gestion des utilisateurs

#creation de la fonction "creation_login"
def creation_login(prenom: str, nom: str):                       
   
    prenom = prenom.strip().lower()                                     #.strip() supprime les espaces à la fin et au début de la variable 
    nom = nom.strip().lower()                                           #.lower() met la chaines de caractère en minuscule

    # Séparation des prénoms par espace ou tiret
    separateurs = [" ", "-"]                                            #Liste d'identification des séparateurs
    for sep in separateurs:
        prenom = prenom.replace(sep, " ")                               #remplace les séparateurs de la liste en espace

    liste_prenoms = prenom.split()                                      #identification des prénoms dans une liste

    # Récupération des initiales 
    initiales = "".join([pldp[0] for pldp in liste_prenoms])            #pldp = première lettre du prénom

    # Construction du login
    login = initiales + "." + nom 

    return login

#creation_login()                                                        #Pour test fonction