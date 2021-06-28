# Dada la clase `ListaEnlazada` con únicamente una referencia al primer nodo
# donde los datos son números enteros, implementar el método `completar_huecos()`, 
# que agrega los nodos necesarios de forma tal de que no queden "huecos", 
# o sea que todos los números sean consecutivos. La función debe ser O(N) en tiempo.
# Por ejemplo, para la lista 1 -> 4 -> 3 -> 1 -> 3, luego de completar_huecos() debería quedar: 
# 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1 -> 2 -> 3.

class _Nodo:
    def __init__(self, dato, prox=None):
        self.prox = prox
        self.dato = dato

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def crear_desde(self, lista):
      for elemento in lista:
        self.append(elemento)

    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def append(self, elemento):
        if not self.prim:
            self.prim = _Nodo(elemento)
            return
        
        actual = self.prim
        while actual.prox:
            actual = actual.prox
        actual.prox = _Nodo(elemento)

    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def __eq__(self, other):
        act = self.prim
        act_other = other.prim

        while act and act_other:
            if act.dato != act_other.dato:
                return False
            act = act.prox
            act_other = act_other.prox
        
        if not act and act_other or not act_other and act:
            return False
        
        return True

    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def __str__(self):
        '''
        Devuelve una representación en la forma {[elem_1] -> [elem_2] -> ... }
        de la lista enlazada.
        '''
        actual = self.prim
        
        s = '{'
        while actual:
            s += f'[{actual.dato}] -> '
            actual = actual.prox
        
        return s.rstrip(' -> ') + '}'

    # Completar el siguiente metodo
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

le = ListaEnlazada()
le_res = ListaEnlazada()
le.crear_desde([1,4,3,1,3])
le_res.crear_desde([1,2,3,4,3,2,1,2,3])
le.completar_huecos()
assert le == le_res