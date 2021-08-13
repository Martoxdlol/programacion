import random

def generar(n):
    return [random.randint(0, 100) for _ in range(n)]

def ordenar(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]

# (tiempo) Es de tipo O(N cuadrado), porque hay dos bucles que recorren N veces y uno esta adentro del otro
# (espacio) Es de tipo O(N), es in-place y no está creando nada que se acumule por cada iteracion 

def pruebas():
    L = [5, 2, 3, 1, 4]
    ordenar(L)
    assert L == [1, 2, 3, 4, 5]

    from timeit import timeit
    for n in [1, 10, 100, 500, 1000, 5000, 10000]:
        print(f"Probando con n = {n}")

        # generamos una lista a ordenar
        L = generar(n)

        # ordenamos y medimos cuánto tiempo tarda
        s = timeit(lambda: ordenar(L), number=1)

        # verificamos que está ordenada
        assert all(L[i] >= L[i-1] for i in range(1, len(L)))

        print(f"  OK -- {s:.2f} segundos")

    from os import path
    print(f"{path.basename(__file__)}: OK")


pruebas()
