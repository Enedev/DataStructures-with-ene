
def f(l, c=0):
  #caso base
  if(len(l) == 0):
    return c
  else:
    #caso recursivo
    l = l[1:]
    c += 1
  return f(l,c)

l = [1,23,2]
print(f(l))