#Defina una función recursiva que reciba una lista para determinar cuántos numeros pares hay en ella

numeros = [1,2,3,4,5,6]

def pares(n):
    if len(n) == 0:
        return 0
    else:
        es_par = n[0] % 2 == 0
        return es_par + pares(n[1:])

print(pares(numeros))