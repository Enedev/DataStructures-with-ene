# Cree una función recursiva que solicite un mensaje al usuario hasta que el usuario ingrese "STOP". Durante el proceso, imprima
# cada palabra. Al final, imprima el tamaño acumulado de todas las palabras. NO recursiva de cola.

def print_msg():
  msg = input("Mensaje: ")
  if(msg == "STOP"):
    return 0
  else:
    #Sí o sí es diferente de stop
    print(msg)
    return len(msg) + print_msg()

print_msg()