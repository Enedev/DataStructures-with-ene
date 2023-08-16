# Defina una función recursiva que reciba un nombre (String) en minúsculas y que lo devuelva con las vocales en mayúsculas

string = "ugu"

def mayus(word, i = 0):
    if(len(word) == i):
        return ""
    else:
        if (word[i] in "aeiou"):
            return word[i].upper() + mayus(word,i+1)
        return word[i] + mayus(word,i+1)
    
print(mayus(string))