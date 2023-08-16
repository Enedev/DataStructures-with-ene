#Escriba una función recursiva que encuentre el mínimo de una lista l dada

def find_minimum_in_list(lst, idx=0, minimum=float('inf')):
    if idx == len(lst):
        return minimum
    
    if lst[idx] < minimum:
        minimum = lst[idx]
    
    return find_minimum_in_list(lst, idx + 1, minimum)

example_list = [8, 3, 12, 6, 1, 9]
minimum_found = find_minimum_in_list(example_list)
print("Minimum of the list:", minimum_found)


#Explicacions inf: Cuando usas float("inf"), estás creando un valor de punto flotante que representa el infinito positivo.
#Esto se utiliza a menudo cuando necesitas inicializar una variable con un valor que está garantizado a ser mayor que cualquier otro valor numérico.