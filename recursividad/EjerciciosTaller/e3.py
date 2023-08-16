#Cree una funcion recursiva de cola que calcule la sumatoria de todos los numeros impares
# de una matriz nxn

def sum_odd_numbers_matrix(matrix, row=0, col=0, total=0):
    if row == len(matrix):
        return total
    if col == len(matrix[0]):
        return sum_odd_numbers_matrix(matrix, row + 1, 0, total)
    if matrix[row][col] % 2 != 0:
        total += matrix[row][col]
    return sum_odd_numbers_matrix(matrix, row, col + 1, total)

matrix = [[1, 2], [3, 3]]
result = sum_odd_numbers_matrix(matrix)
print(f"La sumatoria de los números impares en la matriz es: {result}")
