# Parcial 1 - 14 de mayo de 2021

Algoritmos y programación 1 - Ingeniería informática UBA


### Este es una mejor versión del ej1
```python
def eliminar_multiplos(cadena, n):
    resultado = ''
    for i,c in enumerate(cadena):
        if (i + 1) % n == 0:
            continue

        resultado += c
    return resultado
```

### Este es una mejor versión del ej2
```python
#mentira, me gusta mi solución
```

### Este es una mejor versión del ej3
```python
def eliminar_multiplos_2(lista):
    resultado = []
    for i,v in enumerate(lista):
        if (i+1) % 2 == 0: resultado.append(v)
    return resultado

def elegir_participante(participantes):
    while len(participantes) > 1:
        participantes = eliminar_multiplos_2(participantes)
        participantes.reverse()
    return participantes[0]
```
