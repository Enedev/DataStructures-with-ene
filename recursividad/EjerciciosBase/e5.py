# Escriba una función recursiva que reciba un número y retorne la cantidad de dígitos de este número.

def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

numero_ejemplo = 12345
cantidad_digitos = contar_digitos(numero_ejemplo)
print("Cantidad de dígitos:", cantidad_digitos)
