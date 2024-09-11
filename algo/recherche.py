#Victor Dubost

import random
liste = []
for i in range(int(input("taille de la liste : "))):
    liste.append(random.randint(0, 1000))

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
                nbIterations += 1
    return "nombre itérations tri à bulles : " + str(nbIterations)

print(triBulles(liste))

def triSelection(liste):
    nbIterations = 0
    for i in range(len(liste)):
        min = i
        for j in range(i+1, len(liste)):
            if liste[min] > liste[j]:
                min = j
        liste[i],liste[min] = liste[min],liste[i]
        nbIterations += 1
    return "nombre itérations tri selection: " + str(nbIterations)


print(triSelection(liste))

# pas bon 
def triInsertion(liste):
    nbIterations = 0
    for i in range(len(liste)):
        liste.insert(liste[i],liste[1:liste])
        liste = liste[1:len()]
    # print(liste)
    return "nombre itérations tri insertion : " + str(nbIterations)

# print(triInsertion(liste))