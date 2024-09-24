from random import randint
from random import shuffle

main1 = []
main2 = []
jeu_32 = [
    "As de Trèfle", "Roi de Trèfle", "Dame de Trèfle", "Valet de Trèfle", "10 de Trèfle", "9 de Trèfle", "8 de Trèfle", "7 de Trèfle",
    "As de Carreau", "Roi de Carreau", "Dame de Carreau", "Valet de Carreau", "10 de Carreau", "9 de Carreau", "8 de Carreau", "7 de Carreau",
    "As de Cœur", "Roi de Cœur", "Dame de Cœur", "Valet de Cœur", "10 de Cœur", "9 de Cœur", "8 de Cœur", "7 de Cœur",
    "As de Pique", "Roi de Pique", "Dame de Pique", "Valet de Pique", "10 de Pique", "9 de Pique", "8 de Pique", "7 de Pique"
]

# version 1 : pioche aléatoire dans un jeu trié

def pioche1(nb_carte):                                                   
    for i in range(nb_carte):                                       # pour le nombre de carte à piocher
        main1.append(jeu_32.pop(randint(0, len(jeu_32) - 1)))        # on pioche une carte aléatoire dans le jeu en la retirant en même temps
    return main1, jeu_32

# version 2 : pioche des premières cartes dans un jeu mélangé

def pioche2(nb_carte):
    shuffle(jeu_32)                         # on mélange le jeu une seule fois au début
    for j in range(nb_carte):               
        main2.append(jeu_32.pop())          # on pioche la première carte avec pop() et l'ajoute à la main
    return main2, jeu_32


nb_cartes = int(input("Nombre de cartes : "))

resultat1 = pioche1(nb_cartes)
print("Main1 : ", resultat1[0])
print("Jeu1 : ", resultat1[1])

resultat2 = pioche2(nb_cartes)
print("Main2 : ", resultat2[0])
print("Jeu2 : ", resultat2[1])