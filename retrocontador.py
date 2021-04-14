def retrocontador(e):
#    print('{} '.format(e), end='')
    
    if e > 0:
        retrocontador(e-1)
    
retrocontador(10)

# sumatorio recursivo

def sumatorio(n):
    if n != 0:
        return n + sumatorio(n-1)

# Marca su fin  
    else:
        return 0 

sumatorio(4)

def factorial(n):
    if n != 1:
        return n * factorial(n-1)
    else:
        return 1
    
print(factorial(12))
    