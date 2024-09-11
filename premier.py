from random import*

a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@&%'
def hacker():
    while True :
        ligne = ''
        for i in range(randint(0,120)):
            ligne += a[randint(0,len(a)-1)]
            
        print(ligne)
        ligne = ''


caracteres = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1234567890', '&#@*+']
def mdpgenerator():
    mdp = ''
    l = int(input('Longueur du mot de passe : '))
    c = int(input('complexité (1,2,3,4) : '))-1
    for i in range(int(l)):
        liste = caracteres[randint(0,c)]
        mdp += liste[randint(0,len(liste)-1)]
    return mdp


def posneg():
    n = int(input("nombre : "))
    if n > 0 :
        return "le nombre est positif"
    elif n < 0 :
        return "le nombre est négatif"
    else : 
        return "le nombre est nul"

def imc():
    taille = int(input('taille : '))/100
    poids = int(input('poids : '))
    imc = poids / taille**2
    if imc > 25 :
        return "obésité"
    elif imc < 18.5 :
        return "maigre"
    else :
        return "bonne santé"

def celsiusToKelvin(deg, isCelsius):
    if isCelsius :
        return deg + 273,15
    else :
        return deg - 273,15

def isChauffard():
    km = int(input("distance en m : "))/1000
    h = int(input("temps en s : "))/3600
    v = km/h
    if v > 50 :
        return "chauffard !"
    else :
        return "conduite légale"

print(mdpgenerator())
# hacker()
# print(posneg())
# print(imc())
# print(celsiusToKelvin(14, True))
# print(isChauffard())
# print(heureIsValide({'h':17, 'm':84, 's':32}))