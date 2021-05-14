# Escribir una funcion `dar_vuelta` que reciba una lista de tuplas de numeros y que 
# devuelva una nueva lista de tuplas, donde la primer tupla tendra el primer elemento 
# de todas las tuplas originales; la segunda, los segundos, etc.

# Ejemplo: 
# [(1,2,3), (4,5), (6,), (7,8,9,10)]
#   => 
# [(1,4,6,7), (2,5,8), (3,9), (10,)]

# Nota: las tuplas originales no tienen todas la misma cantidad de elementos entre sí.
# Ayuda: Una tupla de un solo elemento se puede crear de la forma `t = (elem,)`

# Escribir debajo de este comentario el código del ejercicio

def dar_vuelta(lista):
    maxlen = max(map(len, lista))
    resultado = []
    for posicion_en_tupla in range(maxlen):
        lista_temporal = []
        for tupla in lista:
            if posicion_en_tupla < len(tupla):
                lista_temporal.append(tupla[posicion_en_tupla])
        resultado.append(tuple(lista_temporal))
    return resultado

# Pruebas

l_inicial = [(1,2,3), (4,5), (6,), (7,8,9,10)]
l_esperada = [(1,4,6,7), (2,5,8), (3,9), (10,)]
l_resultado = dar_vuelta(l_inicial)

for i in range(len(l_esperada)):
    assert list(l_esperada[i]) == list(l_resultado[i])

# Explicacion de pensamiento
# La lista resultante va a tener de largo lo mismo que la cantidad maxima de valores que tenga alguna de las tuplas. 
# Ej: [(1,2,3),(4,5),(6,7,8,9)] ; la lista resultante va a tener 4 items de largo porque la tercer tupla tiene 4 valores y es la que mas tiene
# Cada item de la lista resultante va a tener un indice (la posicion en la que esta en la lista). Este indice corresponde al indice en cada tupla de la lista original
# Ej: entada = [ ( 1 , 2 )        ,        ( 3 , 4 ) ]              resultante = [ (1,3) , (3,4) ]
#         indice 0 ^   ^ indice 1   indice 0 ^   ^ indice 1                 indice 0 ^       ^ indice 1 