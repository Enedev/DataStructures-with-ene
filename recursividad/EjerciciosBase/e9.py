#E9. Escriba una función recursiva que invierta un string dado

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + reverse_string(string[:-1])

example_string = "Hello world"
reversed_string = reverse_string(example_string)
print("Reversed string:", reversed_string)
