from turtle import *

def py():
    width(5)
    color('red')
    down()
    left(90)
    for i in range (4):
        right(90)
        forward(100)
    backward(100)
    backward(100)

    up()
    right(90)
    forward(200)
    left(90)

    color('blue')
    down()
    forward(130)
    left(45)
    forward(95)
    backward(95)
    right(90)
    forward(95)

def spirale():
    width(5)
    color('green')
    down()
    for i in range(50):
        left(45)
        forward(10*i)

def triangle():
    width(5)
    color('blue')
    down()
    for i in range(3):
        forward(360)
        left(120)
        for j in range(3):
            forward(180)
            left(120)
            for k in range(3):
                forward(90)
                left(120)

def initTakuzuCorrect () :
    matrice = list ([[0, 1, 1, 0], 
                     [1, 0, 0, 1],
                     [0, 0, 1, 1],
                     [1, 1, 0, 0]] )
    
    return matrice

def initTakuzuNonCorrect () :
    matrice = list ([[0, 1, 1, 1], 
                     [1, 0, 0, 1],
                     [0, 0, 1, 1],
                     [1, 1, 0, 0]] )
    return matrice

def verifTakuzu(matrice):
    nb = len(matrice)/2
    for i in range(len(matrice)):
        l1, l2 = 0, 0
        for j in range(len(matrice)):
            l1 += matrice[i][j]
            l2 += matrice[j][i]
        if l1 != nb or l2 != nb : return False
    return True

# py()
# spirale()
# triangle()
# print(verifTakuzu(initTakuzuCorrect()))
# print(verifTakuzu(initTakuzuNonCorrect()))