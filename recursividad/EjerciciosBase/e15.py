#Dada una matriz M de nxn imprima los elementos de su diagonal principal usando una función recursiva

def print_diagonal(matrix, row=0, col=0):
    n = len(matrix)
    
    if row >= n or col >= n:
        return
    
    print(matrix[row][col])
    print_diagonal(matrix, row + 1, col + 1)

# Ejemplo de matriz cuadrada
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_diagonal(matrix)
