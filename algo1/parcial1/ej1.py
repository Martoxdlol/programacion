# Escribir una función que recibe una cadena y un numero n 
# y devuelve la cadena eliminando los caracteres en todas 
# las posiciones multiplos de n, contando las posiciones desde 1.
# Ejemplo: con la cadena 'abcdefghijk' y n=3 debe devolver 'abdeghjk'

# Escribir debajo de este comentario el código del ejercicio

def eliminar_multiplos(cadena, n):
    eliminados = 0
    lista = list(cadena)
    while True:
        i = (n - 1) * (eliminados + 1) # (n - 1) Es el ancho de cada 'bloque' eliminado. (n - 1) * eliminados es la cantidad de string que ya hicimos modificar. 
        if i >= len(lista): break
        lista.pop(i)
        eliminados += 1
    return "".join(lista)

# Pruebas

assert eliminar_multiplos('abcdefghijk', 3) == 'abdeghjk'
assert eliminar_multiplos('abcdefghijk', 12) == 'abcdefghijk'
assert eliminar_multiplos('01234567890123456789', 5) == '0123567801235678'
assert eliminar_multiplos('012345678901234567891', 5) == '01235678012356781'
assert eliminar_multiplos('0123456789012345678912', 5) == '012356780123567812'
assert eliminar_multiplos('012345678901234567891234', 5) == '01235678012356781234'
assert not eliminar_multiplos('0123456789012345678912345', 5) == '012356780123567812345'

#IGNORAR, me sirve para pensar (n = 3)
#abCdefghijk | indice: (3-1)*1 = 2
#ab deFghijk | indice: (3-1)*2 = 4 
#ab de ghIjk | indice: (3-1)*3 = 6