#factorial con tabulación
def tabfact(n):
  fact = [1] * (n+1)
  fact[0] = 1
  for i in range(1, n+1):
    fact[i] = i * fact[i-1]
  return fact[n]


print(tabfact(4))
