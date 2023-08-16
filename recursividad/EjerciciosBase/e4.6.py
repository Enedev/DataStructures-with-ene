#E4.6 Cree una función recursiva para imprimir todos los elementos de una matriz

def imprimir_matriz(matriz, fila=0, columna=0):
    if fila == len(matriz):
        return ""
    
    print(matriz[fila][columna], end=' ')
    
    if columna + 1 < len(matriz[fila]):
        imprimir_matriz(matriz, fila, columna + 1)
    else:
        imprimir_matriz(matriz, fila + 1, 0)

matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

imprimir_matriz(matriz_ejemplo)
