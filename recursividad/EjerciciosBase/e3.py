#Defina una función recursiva que reciba un string de números separados por coma, por ejemplo "1,2,3, 4,5"
# y devuelva la productoria de estos números. Tenga en cuenta el caso en que hay y no hay espacios entre los números y las comas.


s = "1,2,3,     ñ            3,3,3,3,,,,,,4333 3 3 3 3     3453    4,5"
def f(s, idx=0, total=1):
  if(s == ""):
    return 0
  if(idx == len(s)):
    return total
  else:
    if(s[idx] in "1234567890"):
      total *= int(s[idx])
    return f(s, idx+1, total)

print(f(s))