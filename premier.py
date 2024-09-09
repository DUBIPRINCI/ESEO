from random import*

a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@&%'
def hacker():
    while True :
        ligne = ''
        for i in range(randint(0,120)):
            ligne += a[randint(0,len(a)-1)]
            
        print(ligne)
        ligne = ''

# hacker()

caracteres = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1234567890', '&#@*+']
def mdpgenerator():
    mdp = ''
    l = int(input('Longueur du mot de passe : '))
    c = int(input('complexité (1,2,3,4) : '))-1
    for i in range(int(l)):
        liste = caracteres[randint(0,c)]
        mdp += liste[randint(0,len(liste)-1)]
    return mdp

# print(mdpgenerator())