#Crea una funcion recursiva que no sea de cola, y que 
#invierta solo la mitad de un string, por ejemplo si es "hola", que retorne "hoal"

def reverse_half_string(s):
    if len(s) <= 1:
        return s

    middle = len(s) // 2
    first_half = s[:middle]
    second_half = s[middle:]
    reversed_second_half = second_half[::-1]
    
    return first_half + reversed_second_half

input_str = input("Ingrese una cadena: ")
result = reverse_half_string(input_str)
print(f"Solucion del ::-1 Cadena con mitad derecha invertida: {result}")

#Sin el reversed_second_half = second_half[::-1]

def reverse_half_string_with_for(s):
    if len(s) <= 1:
        return s

    middle = len(s) // 2
    left_half = s[:middle]
    right_half = s[middle:]

    reversed_right_half = ""
    for i in range(len(right_half) - 1, -1, -1):
        reversed_right_half += right_half[i]

    return left_half + reversed_right_half

result_for = reverse_half_string_with_for(input_str)
print(f"Cadena con mitad derecha invertida (con for): {result_for}")


#Solucion sin for

def reverse_half_string_good(s, idx=0):
    if(idx==len(s)):
        return ""
    if(idx < len(s) // 2):
        return s[idx] + reverse_half_string_good(s,idx+1)
    else:
        return reverse_half_string_good(s, idx+1) + s[idx]

result = reverse_half_string(input_str)
print(f"Solucion correcta para jhonathan con mitad derecha invertida: {result}")








