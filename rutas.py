
#Tarea corta 08
#Analisis de algoritmos
#Jose Alexander Artavia Quesada
#2015098028

import numpy as np


"""
    Funcion que valida si las matriz de entrada cumple con los
    requerimientos para encontrar una ruta
    E: Una matriz
    S: Llama a una funcion aux para calcular la ruta
"""
def contar_rutas_mas_cortas(C):
    
    filas = len(C)
    columnas = len(C[0])

    inicio = C[0][0]
    fin = C[filas - 1][columnas - 1]

    #Inicio o final, sin ruta
    if inicio == 1 or fin == 1:
        return 0

    #Las dos opciones iniciales de inicio en 1, sin ruta
    elif C[0][1] == 1 and C[1][0]== 1:
        return 0

    else:
        return contar_rutas_mas_cortas_aux(C,filas,columnas)

#-----------------------------------------------------------------------#    

"""
    Funcion que va sumando las posibles rutas en la posicion [i] [j], con respecto
    a los valores de una posicion de arriba y derecha de su posicion
    E: Una matriz, largo fila, largo columnas
    S: Llama a una funcion aux para calcular la ruta
"""

def contar_rutas_mas_cortas_aux(matriz,filas,columnas):
    
    #Revisa la fila 0
    #Bandera = 1, los siguientes 0 quedan igual
    bandera = 0
    for i in range(columnas):
        actualFilaCero = matriz[0][i]
        if actualFilaCero == 0 and bandera == 0:
            matriz[0][i] = 1
        else:
            bandera = 1
            matriz[0][i] = 0

    
    #Revisa la columna 0
    bandera = 0
    for i in range(1, filas):
        actualColumnaCero = matriz[i][0]
        if actualColumnaCero == 0 and bandera == 0:
            matriz[i][0] = 1
        else:
            bandera = 1
            matriz[i][0] = 0
            
    #Suma la posicion actual con el de la derecha y arriba
    for i in range(1, filas):
        for j in range(1, columnas):
            if matriz[i][j] != 1:
                matriz[i][j] = matriz[i - 1][j] + matriz[i][j - 1]
            else:
                matriz[i][j] = 0

    #imprmir = np.array(matriz)
    #print(imprmir, "\n")

    return matriz[filas - 1][columnas - 1]

"""
C =[[0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

print(contar_rutas_mas_cortas(C))
"""
#raise NotImplementedError()
