# reduce no le aplica la función al primer número de la lista para funciones dobles. 

from functools import reduce

def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
        
    return resultado

def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor*2
        
    return resultado

def ProductoTotal(l):
    resultado = 0
    for valor in l:
        resultado *= valor
    return resultado


lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)

# Creo una copia de la lista.

l = lista[:]

# Añado el neutro para la suma en la posición cero: lista = [0, 1, 3, -1, 15, 9]
# Como reduce no afecta al primero, si metemos el cero, entonces ahora si que afecta al 1. 

l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x + y*2, l)



print(sumatorio)
print(sumatorioDobles)


        
    