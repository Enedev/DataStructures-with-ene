#E10. Escriba una función recursiva para determinar si un número n es primo o no

def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)

number = 17
if is_prime(number):
    print(number, "esta en su prime(primo).")
else:
    print(number, "no esta en su prime (primo).")
