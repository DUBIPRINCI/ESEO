def dichotomie(n, liste):
    debut = 0
    fin = len(liste) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if liste[m] == n:
            return True
        elif liste[m] < n:
            debut = m + 1
        else:
            fin = m - 1
    return False



print(dichotomie(13, [1,2,4,6,9,12,15,20,21,22,23,25,30]))