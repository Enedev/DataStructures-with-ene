#E4.5 Dada una matriz m y un elemento e, determine cuántas veces está e en la matriz

def count_in_matrix(m, e, idx=0):
  print(m[idx])
  #casos base
  if(len(m) == 0): return False
  if(e in m[idx]): return True
  #caso recursivo
  if(idx < len(m)-1):
    return count_in_matrix(m,e,idx+1)
  else:
    return False
m = [[1,2],[2,5]]
print(count_in_matrix(m, 2))