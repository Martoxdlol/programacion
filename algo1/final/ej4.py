class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox


class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def lshift(self, n):
        ultimo = self.prim
        while ultimo.prox:
            ultimo = ultimo.prox
        for _ in range(n):
            ultimo.prox, self.prim = self.prim, self.prim.prox
            ultimo = ultimo.prox
            ultimo.prox = None


def pruebas():

    # creamos "a mano" la lista [3] -> [5] -> [8] -> [11]
    n3 = _Nodo(11, None)
    n2 = _Nodo(8, n3)
    n1 = _Nodo(5, n2)
    n0 = _Nodo(3, n1)
    lista = ListaEnlazada()
    lista.prim = n0

    lista.lshift(3)

    assert lista.prim.dato == 11
    assert lista.prim.prox.dato == 3
    assert lista.prim.prox.prox.dato == 5
    assert lista.prim.prox.prox.prox.dato == 8

    # OPCIONAL: Pruebas adicionales

    lista.prim = _Nodo(1, _Nodo(2, _Nodo(3, _Nodo(4, _Nodo(5, _Nodo(6, None))))))
    assert lista.prim.dato == 1
    assert lista.prim.prox.dato == 2
    assert lista.prim.prox.prox.dato == 3
    assert lista.prim.prox.prox.prox.dato == 4
    assert lista.prim.prox.prox.prox.prox.dato == 5
    assert lista.prim.prox.prox.prox.prox.prox.dato == 6
    lista.lshift(1)
    assert lista.prim.dato == 2
    assert lista.prim.prox.dato == 3
    assert lista.prim.prox.prox.dato == 4
    assert lista.prim.prox.prox.prox.dato == 5
    assert lista.prim.prox.prox.prox.prox.dato == 6
    assert lista.prim.prox.prox.prox.prox.prox.dato == 1
    lista.lshift(6)
    assert lista.prim.dato == 2
    assert lista.prim.prox.dato == 3
    assert lista.prim.prox.prox.dato == 4
    assert lista.prim.prox.prox.prox.dato == 5
    assert lista.prim.prox.prox.prox.prox.dato == 6
    assert lista.prim.prox.prox.prox.prox.prox.dato == 1
    lista.lshift(8)
    assert lista.prim.dato == 4
    assert lista.prim.prox.dato == 5
    assert lista.prim.prox.prox.dato == 6
    assert lista.prim.prox.prox.prox.dato == 1
    assert lista.prim.prox.prox.prox.prox.dato == 2
    assert lista.prim.prox.prox.prox.prox.prox.dato == 3

    from os import path
    print(f"{path.basename(__file__)}: OK")


pruebas()
