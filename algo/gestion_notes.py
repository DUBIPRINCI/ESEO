dictionnaire = {"Patrick": 4, "Antoine": 12, "Robert": 0,"Olivier1":15, "Olivier2": 8, "Camille": 7, "Jean":20, "Xavier":11, "Sophie":20, "Alain":0, "Sofia":12}

def moyenne():
    moy = 0
    for valeur in dictionnaire.values():
        moy += valeur
    return moy / len(dictionnaire)

# print(moyenne())

def isAdmis():
    liste_admis = []
    liste_recalés = []
    liste_absents = []
    for cle, valeur in dictionnaire.items():
        if valeur >= 10:
            # print(cle + ' est admis')
            liste_admis.append(cle)
        elif valeur == 0 :
            # print(cle + ' est absent')
            liste_absents.append(cle)
        else :
            # print(cle + ' est recalé')
            liste_recalés.append(cle)

    for j in liste_absents:
        dictionnaire.pop(j)
        
    return liste_admis, liste_recalés, liste_absents


def addNote(nom, note):
    dictionnaire[nom] = note

addNote(input("nom : "), int(input("note : ")))
admis, recalés, absents = isAdmis()
print("admis : ", admis)
print("recalés : ", recalés)
print("absents : ", absents)
print('liste sans absent :', dictionnaire)