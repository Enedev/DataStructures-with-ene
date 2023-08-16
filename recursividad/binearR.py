import random
random.seed(0)
s = random.sample(list(range(10000)),500) #Lista generada aleatoriamente, 500 datos
sum_s = sum(s[:5]) 

def binary_sum(s,start,end):
  if(start>=end): #No hay elementos en la lista
    return 0
  elif(start == end-1): #Sólo queda un elemento
    return s[start]
  else: #Dos o más elementos
    mid = (start+end)//2
    return binary_sum(s, start, mid) + binary_sum(s, mid, end)

assert sum_s == binary_sum(s,0,5), "Error" #Evaluación de caso de prueba
print(binary_sum(s,0,5))