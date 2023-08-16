#Cree una funcion recursiva que reciba una lista "l", un elemento "e" y un indice "i" y que retorne si el
# elemento "e" esta en la lista "l" en la posicion "i".

l = [1,2,3]
e = 2
i = 0


#Deberia retornar false porque en la posicion 0 de l no hay un 2

def element_at_position(lst, element, index, current_index=0):
    if current_index == index:
        return lst[current_index] == element
    if current_index >= len(lst):
        return False
    return element_at_position(lst, element, index, current_index + 1)

result = element_at_position(l, e, i)
print(result) 