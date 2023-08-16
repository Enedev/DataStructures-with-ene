# Escriba una función recursiva que encuentre el mínimo común múltiplo de dos números n y m.

def calcular_mcd(a, b):
    if b == 0:
        return a
    else:
        return calcular_mcd(b, a % b)

def calcular_mcm(n, m):
    mcd = calcular_mcd(n, m)
    return (n * m) // mcd

n = 12
m = 18
mcm = calcular_mcm(n, m)
print("Mínimo Común Múltiplo:", mcm)
