# Escriba una función recursiva que sume los dígitos de un número dado.

def sumar_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)

numero_ejemplo = 12345
suma_digitos = sumar_digitos(numero_ejemplo)
print("Suma de dígitos:", suma_digitos)
