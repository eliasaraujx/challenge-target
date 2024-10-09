def fibonacci(num):
    a, b = 0, 1
    
    if num == 0 or num == 1:
        return f"{num} pertence à sequência de Fibonacci."
    
    while b < num:
        a, b = b, a + b
        
    if  b == num:
        return f"{num} pertence à sequência de Fibonacci"
    else:
        return f"{num} não pertence à sequência de Fibonacci"


num = 21 
print(fibonacci(num))   