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

# print(dichotomie(13, [1,2,4,6,9,12,15,20,21,22,23,25,30]))

def triBulles(liste):
    nbIterations = 0
    for i in range(len(liste)):
        for j in range(i, len(liste)):
            if liste[j] < liste[i]:
                liste[i],liste[j] = liste[j],liste[i]
                print(liste)
                nbIterations += 1
    return "nombre itérations : " + str(nbIterations)

print(triBulles([12,52,63,97,54,29,91,24,38,46]))

def triSelection(liste):
    nbIterations = 0
    for i in range(len(liste)):
        min = i
        for j in range(i+1, len(liste)):
            if liste[min] > liste[j]:
                min = j
        liste[i],liste[min] = liste[min],liste[i]
        print(liste)
        nbIterations += 1
    return "nombre itérations : " + str(nbIterations)


print(triSelection([12,52,63,97,54,29,91,24,38,46]))