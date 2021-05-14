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
