#E11. Escriba una función recursiva que reciba una lista de palabras
#y retorne una lista con las palabras que contengan mayúsculas y otra lista con las que no tienen.

def categorize_words(words, with_upper=[], without_upper=[], idx=0):
    if idx == len(words):
        return with_upper, without_upper
    
    if any(c.isupper() for c in words[idx]):
        with_upper.append(words[idx])
    else:
        without_upper.append(words[idx])
    
    return categorize_words(words, with_upper, without_upper, idx + 1)

word_list = ["Hello", "world", "Python", "programming", "UPPERCASE"]
with_uppercase, without_uppercase = categorize_words(word_list)
print("Words with uppercase:", with_uppercase)
print("Words without uppercase:", without_uppercase)

#chat gpt al fallo