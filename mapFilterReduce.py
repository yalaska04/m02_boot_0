from functools import reduce

lista = [1, 3, -1, 15, 9]

def doble(x):
    return x+x

# operador map --> aplica lambda a cada uno de los elementos de la lista
listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble,lista)

def esPar(x):
    return x % 2 == 0

# operador filter -->  para meter funciones anonimas con condición if.
# Si condición es verdadera return x/ si no return None.
# filtra los valores, solo deja pasar los cumplen la condición.

listaPares = filter(lambda x: x % 2 == 0, lista)

# No va a funcionar, porque la función dentro del filter tiene que ser una que devuelva TRUE/FALSE
listaPares1 = filter(esPar,lista)

# Reduce --> first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.

sumatorio = reduce(lambda x, y: x + y, lista)
sumatorioDobles = reduce(lambda x, y: x + y*2, lista)
suma100 = reduce(lambda x, y: x+y, range(101))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)
print(suma100)