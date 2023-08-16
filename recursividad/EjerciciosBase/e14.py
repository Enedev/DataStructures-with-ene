#Escriba una función que reciba una listas de listas, por ejemplo [[1,2],[[[[[1,2,[3,4]]],2],2]],4]
# e impriman todos los numeros atrapados

def print_nested_numbers(lst):
    for item in lst:
        if isinstance(item, list):
            print_nested_numbers(item)
        else:
            if isinstance(item, int):
                print(item)

nested_list = [[1, 2], [[[[[1, 2, [3, 4]]], 2], 2]], 4]
print_nested_numbers(nested_list)

#Explicacion isistance()
# isinstance(element, list) devuelve True. Si element no fuera una lista, se imprimiría "element is not a list".