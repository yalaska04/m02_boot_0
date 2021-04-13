
def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
            
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
            
    return m
    
def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0 
    for valor in l:
        suma += valor
        
    return suma / len(l)


funciones = {
    'max': maxi,
    'min': mini,
    'med': media
}

# función de primer nivel que me devuelve una función.

def returnF(nombre):
    nombre = nombre.lower()
    if nombre.lower() in funciones.keys():
        return funciones[nombre]
    
    return None

print(maxi(1,3,-1,15,9))
print(mini(1,3,-1,15,9))
print(media(1,3,-1,15,9))

print(returnF('max')(1,3,-1,15,9))