arrayExample = [1,2,3]

def sumaArray(x):

    if len(x) != 0:
        return x.pop(0) + sumaArray(x)
    else:
        return 0
print(sumaArray(arrayExample))


