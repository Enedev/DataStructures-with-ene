#Cree una función recursiva que reciba una lista de números y retorne una nueva lista 
#con subgrupos (listas) de cada número. Por ejemplo: la lista [1,1,2,3,3] debe retornar [[1,1],[2],[3,3]]

def create_subgroups(numbers, subgroups=None, idx=0):
    if subgroups is None:
        subgroups = []
    
    if idx == len(numbers):
        return subgroups
    
    if idx == 0 or numbers[idx] != numbers[idx - 1]:
        subgroups.append([numbers[idx]])
    else:
        subgroups[-1].append(numbers[idx])
    
    return create_subgroups(numbers, subgroups, idx + 1)

number_list = [1, 1, 2, 3, 3]
subgroups_list = create_subgroups(number_list)
print(subgroups_list)   

