#E1. Cree una función sin recursión de cola que reciba dos matrices mxn y devuelva sin son exactamente 
#iguales, es decir, contienen la misma cantidad de elementos y los mismos elementos en el mismo orden.

def equalsMatrix(matriz1, matriz2, row=0, col=0):
    if row == len(matriz1):
        return True
    
    if col == len(matriz1[row]):
        return equalsMatrix(matriz1, matriz2, row + 1, 0)
    
    if matriz1[row][col] != matriz2[row][col]:
        return False
    
    return equalsMatrix(matriz1, matriz2, row, col + 1)

m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [0, 1, 0, 1]]
m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [0, 1, 0, 1]]
print(equalsMatrix(m1, m2))  

m3 = [[1, 2], [5, 6], [0, 1]]
m4 = [[1, 2], [5, 6], [0, 1]]
print(equalsMatrix(m3, m4))  

m5 = []
m6 = []
print(equalsMatrix(m5, m6)) 

m7 = [[1, 2], [6, 6], [0, 1]]
m8 = [[1, 2], [5, 6], [0, 1]]
print(equalsMatrix(m7, m8))  
