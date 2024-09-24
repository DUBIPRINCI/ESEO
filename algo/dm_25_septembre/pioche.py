from random import randint

main = []
jeu_32 = [
    "As de Trèfle", "Roi de Trèfle", "Dame de Trèfle", "Valet de Trèfle", "10 de Trèfle", "9 de Trèfle", "8 de Trèfle", "7 de Trèfle",
    "As de Carreau", "Roi de Carreau", "Dame de Carreau", "Valet de Carreau", "10 de Carreau", "9 de Carreau", "8 de Carreau", "7 de Carreau",
    "As de Cœur", "Roi de Cœur", "Dame de Cœur", "Valet de Cœur", "10 de Cœur", "9 de Cœur", "8 de Cœur", "7 de Cœur",
    "As de Pique", "Roi de Pique", "Dame de Pique", "Valet de Pique", "10 de Pique", "9 de Pique", "8 de Pique", "7 de Pique"
]


def pioche(nb_carte):                                                   
    for i in range(nb_carte):                                       # pour le nombre de carte à piocher
        main.append(jeu_32.pop(randint(0, len(jeu_32) - 1)))        # on pioche une carte aléatoire dans le jeu en la retirant en même temps
    return main, jeu_32

pioche = pioche(int(input("Nombre de cartes : ")))
print("Main : " + str(pioche[0]))
print("Jeu : " + str(pioche[1]))