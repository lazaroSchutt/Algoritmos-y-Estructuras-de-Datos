# 5. Desarrollar una función que permita convertir un número romano en un número decimal
def romano(num, n, decimal):
    if (n==(len(num)-1)):
        return decimal[num[n]]
    else:
        letra_actual = decimal[num[n]]
        letra_siguiente = decimal[num[n+1]]
        if (letra_actual < letra_siguiente):
            return  -letra_actual + romano(num, n+1, decimal)
        elif (letra_actual >= letra_siguiente):
            return  letra_actual + romano(num, n+1, decimal)

decimal={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
num = "mldxvi" 
num =num.upper()
n = 0
# print (romano(num,n, decimal))

# 8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def binario (decimal):
    if (decimal==1):
        return "1"
    else:
        return str(decimal % 2) + binario(decimal//2)

decimal=10
# print (binario(int(decimal))[::-1])

# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el 
# que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar 
# una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar 
# las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más 
# objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.
mochila=["qsy", "mee", "lol","2","3"]
n=(len(mochila)-1)
def usar_la_fuerza (n, obj):
    if (obj[n] == "sable de luz") or (n==0):
        return n
    else:
        return 0 + usar_la_fuerza(n-1, obj)

m=usar_la_fuerza(n, mochila)
# if (mochila[m]=="sable de luz"):
#     print (f"el sable de luz fue encontrado despues de sacar {n-m} objetos")
# else:
#     print ("el sable de luz no fue encontrado")


# 23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
# matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
# y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
# avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo
lab= [[1,1,0,0],
      [0,1,0,1],
      [1,1,0,1],
      [0,1,1,-1]]
def laberinto(lab, x, y, camino):
    if(x >= 0 and x <= len(lab)-1) and (y >= 0 and y <= len(lab[0])-1):
        if(lab[x][y] == -1):
            camino.append([x, y])
            print(f"Saliste del laberinto el camino es:{camino}")
            camino.pop()
        elif(lab[x][y] == 1):
            camino.append([x, y])
            lab[x][y] = 3
            laberinto(lab, x, y+1, camino)
            laberinto(lab, x, y-1, camino)
            laberinto(lab, x-1, y, camino)
            laberinto(lab, x+1, y, camino)
            camino.pop()
            lab[x][y] = 1

vec=[]
# laberinto(lab, 0, 0,vec)
