# Parcial 3 - 28 de junio de 2021

Algoritmos y programación 1 - Ingeniería informática UBA

Las consignas están en los archivos

## Ej 1
```python
class ListaEnlazada:
    ...

    def completar_huecos(self):
        actual = self.prim
        while True:
            if not actual.prox:
                break
            if actual.dato < actual.prox.dato - 1:
                actual.prox = _Nodo(actual.dato + 1, actual.prox)
            elif actual.dato > actual.prox.dato + 1:
                actual.prox = _Nodo(actual.dato - 1, actual.prox)
            actual = actual.prox
```

## Ej 2
```python
def invertir_primeros_k(cola, k):
    pila_invertidos = Pila()
    cola_auxiliar = Cola()
    for i in range(k):
        pila_invertidos.apilar(cola.desencolar())
    while not cola.esta_vacia():
        cola_auxiliar.encolar(cola.desencolar())
    while not pila_invertidos.esta_vacia():
        cola.encolar(pila_invertidos.desapilar())
    while not cola_auxiliar.esta_vacia():
        cola.encolar(cola_auxiliar.desencolar())
```

## Ej 3
```python
#Solución linda sin pils ni colas
def obtener_suma_maxima(arr, k):
    if k > len(arr):
        k = len(arr)
    suma = 0
    valor_max = 0
    for i in range(k):
        suma += arr[i]
    valor_max = suma
    for i in range(k, len(arr)):
        print(i, i-k)
        suma -= arr[i-k]
        suma += arr[i]
        if suma > valor_max:
            valor_max = suma
    return valor_max



#Solución que te hace la cola
def obtener_suma_maxima(arr, k):
    '''
    EJ:
    k = 3:
    len(arr) => 10

    cola_k = [1,2,3]   colar_arr = [4,5,6,7,8,9,10] suma = 1+2+3

    cola_k = [2,3,4]   colar_arr = [5,6,7,8,9,10]    suma = suma - 1 + 4    es suma mayor al max?
    cola_k = [3,4,5]   colar_arr = [6,7,8,9,10]    suma = suma - 2 + 5      es suma mayor al max?
    cola_k = [4,5,6]   colar_arr = [7,8,9,10]    suma = ...             es suma mayor al max?
    cola_k = [5,6,7]   colar_arr = [8,9,10] ...                     ...
    cola_k = [6,7,8]   colar_arr = [9,10] ...                     ...    
    cola_k = [7,8,9]   colar_arr = [10] ...                     ...
    cola_k = [7,8,9]   colar_arr = [10] ...
    cola_k = [8,9,10]   colar_arr = []    suma = suma - 9 + 10              ...
    '''
    cola_k = Cola()
    cola_arr = Cola()
    suma = 0
    len_cola_k = 0
    for elem in arr: #Se podria hacer con dos for con range de 0 a k-1 y de k a len(arr) pero haciendo eso se puede hacer sin usar colas ni pilas y tengo que usarlas para algo
        if len_cola_k < k:
            len_cola_k += 1
            cola_k.encolar(elem)
            suma += elem
        else:
            cola_arr.encolar(elem)
    valor_max = suma
    while not cola_arr.esta_vacia():
        suma -= cola_k.desencolar()
        suma += cola_arr.ver_frente()
        cola_k.encolar(cola_arr.desencolar())
        if suma > valor_max:
            valor_max = suma
    return valor_max
```
