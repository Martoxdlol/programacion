# Escribir una función `invertir_primeros_k` que recibe una cola y un numero `k`,
# e invierta el orden de los primeros `k` elementos a salir de la cola.
# Ejemplos:
# Para la cola:
# sale <| 1  2  3  4  5 |< entra
# y un k = 3, debería resultar en:
# sale <| 3  2  1  4  5 |< entra
# Para la cola:
# sale <| 1  2  3  4  5 |< entra
# y un k = 7, debería resultar en:
# sale <| 5  4  3  2  1 |< entra

from tda import Cola, Pila

#Completar la siguiente funcion
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


cola = Cola()
cola.encolar_desde([1, 2, 3, 4, 5])
cola_res = Cola()
cola_res.encolar_desde([3, 2, 1, 4, 5])
invertir_primeros_k(cola, 3)
assert cola == cola_res
