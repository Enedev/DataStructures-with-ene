#E12. Escriba una función recursiva que reciba un srtring alfanumérico y 
#retorne el máximo de los dígitos en el string. Por ejemplo: en el string "hola123" debe retornar 3 ya que el máximo digito es 3

def max_digit_in_string(s, idx=0, max_digit=-1):
    if idx == len(s):
        return max_digit
    
    if s[idx].isdigit():
        digit = int(s[idx])
        max_digit = max(max_digit, digit)
    
    return max_digit_in_string(s, idx + 1, max_digit)

alphanumeric_string = "hola123"
max_digit = max_digit_in_string(alphanumeric_string)
print("Maximum digit:", max_digit)
