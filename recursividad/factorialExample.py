def factorial(x):
    
    if x > 1:
         return x * factorial(x-1)
    else:
         return 1
    
print(factorial(5))




def operation(a, b, c ):
     if c == "+":
          result = a + b
     elif c == "-":
          result = a - b
     elif c == "*":
          result = a * b
     elif c == "/":
          result = a / b
     
     return result

print(operation(2,3,"+"))
     