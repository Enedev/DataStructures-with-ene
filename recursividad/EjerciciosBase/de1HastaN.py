def print_1ton(n,c=0):
  if(c != n):
    print_1ton(n, c+1)
    print(c+1)
print_1ton(9)

print("espacio")
def print_1ton(i,n):
  if(i==n):
    print(i)
  else:
    print(n)
    n = n -1
    print_1ton(i,n)

print_1ton(1,10)