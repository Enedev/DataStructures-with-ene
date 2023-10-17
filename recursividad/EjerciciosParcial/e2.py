#E4. Escriba una función no recursiva de cola que reciba una lista
#llena de 1s y 0s y que devuelva cuántos 1s hay en posiciones impares. Asuma la posición 0 como par.

#Como lo quiere Jhonathan:

def find_oddOneWithRules(array, idx=1):
    if idx >= len(array):
        return 0

    count = 1 if array[idx] == 1 else 0
    return count + find_oddOneWithRules(array, idx + 2)

print("Solucion con estandares correctos para Jhonathan")
m1 = [1, 0, 1, 1]
print(find_oddOneWithRules(m1))

m2 = [0, 0, 0, 0]
print(find_oddOneWithRules(m2))

print("Mi solucion inicial")

def find_oddOne(array,idx=1):
    if idx >= len(array):
        return 0

    count = array[idx] + find_oddOne(array, idx + 2)
    return count

m1 = [1, 0, 1, 1]
print(find_oddOne(m1)) 

m2 = [0, 0, 0, 0]
print(find_oddOne(m2))  


