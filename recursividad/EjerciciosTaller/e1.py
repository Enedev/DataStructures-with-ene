#cree una funcion recursiva de cola que reciba un entero y retorne cuantos
# digitos de este numero son multiplos de 2 y 4, ignore el 0


def count_multiples_of_2_and_4_recursive(number):
    if number == 0:
        return 0
    
    digit = number % 10
    count = 0
    
    if digit != 0 and (digit % 2 == 0 and digit % 4 == 0):
        count = 1
    
    return count + count_multiples_of_2_and_4_recursive(number // 10)

num = int(input("Ingrese un número entero: "))
result = count_multiples_of_2_and_4_recursive(num)
print(f"El número contiene {result} dígito(s) múltiplo(s) de 2 y 4 (excepto 0).")

