def jours_par_mois(mois):           # retourne le nombre de jour dans le mois
    if mois in [4, 6, 9, 11]:
        return 30
    elif mois == 2:
        return 28
    else:
        return 31

def prochain_jour(jour, mois, annee):
    if jour < jours_par_mois(mois):             # vérifie si on n'a pas atteint la fin du mois
        return jour + 1, mois, annee            # si ce n'est pas le dernier jour du mois, incrémente simplement le jour
    else:                                       
        jour = 1                                # si on est au dernier jour du mois, on remet le jour à 1
        mois += 1                               # on passe au mois suivant
        if mois > 12:                           # si on dépasse le mois de décembre, on passe à l'année suivante
            mois = 1
            annee += 1
        return jour, mois, annee                # retourne le jour, le mois et l'année mis à jour

def afficher_semaine(jour, mois, annee):
    tableau_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    tableau_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    
    for i in range(7):                                                                          # On parcours les 7 jours de la semaine
        print(f"{tableau_jours[i]} {jour:02d} {tableau_mois[mois - 1]} {annee}")
        jour, mois, annee = prochain_jour(jour, mois, annee)

afficher_semaine(int(input("Jour : ")), int(input("Mois : ")), int(input("Année : ")))