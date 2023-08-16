# Escriba una función recursiva que imprima los números desde un número n hasta otro número m descendentemente.

def imprimir_descendente(n, m):
    if n >= m:
        print(n, end=' ')
        imprimir_descendente(n - 1, m)

n = 10  # Número inicial
m = 5   # Número final
imprimir_descendente(n, m)
