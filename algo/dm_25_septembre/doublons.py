def supprimer_doublons(liste):
    i = 0
    while i < len(liste):               # pour chaque element de la liste
        j = i + 1
        while j < len(liste):           # pour le reste des éléments de la liste
            if liste[i] == liste[j]:    # on vérifie si ils sont égaux
                liste.pop(j)            # si oui, on le retire
            else:
                j += 1                  # sinon on continue avec le suivant
        i += 1                          # on rajoute 1 pour passer au nombre a vérifier suivant
    return liste

print(supprimer_doublons([1,1,2,2,3,4,5,5,6,7,7,8,9,10]))


#  Deuxième version plus optimale car l'on parcours moins la liste

def supprimer_doublons2(liste):                 # autre version enn créant une deuxième liste
    resultat = []
    for element in liste:                       # pour chaque element de la liste
        if element not in resultat:             # on vérifie qu'il n'est pas déja  dans la nouvelle liste
            resultat.append(element)            # si il n'y est pas encore, on l'ajoute dedans
    return resultat

print(supprimer_doublons2([1,1,2,2,3,4,5,5,6,7,7,8,9,10]))