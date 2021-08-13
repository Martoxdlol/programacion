def _merge(a, b, resultado, i1, i2):
    if len(a) == i1 or len(b) == i2:
        resultado += a[i1:]
        resultado += b[i2:]
        return resultado

    if a[i1] < b[i2]:
        resultado.append(a[i1])
        i1 += 1
    else:
        resultado.append(b[i2])
        i2 += 1
    return _merge(a, b, resultado, i1, i2)


def merge(a, b):
    return _merge(a, b, [], 0, 0)


def pruebas():
    assert merge([2, 4, 6, 8], [1, 3, 5, 7]) == [1, 2, 3, 4, 5, 6, 7, 8]

    # OPCIONAL: pruebas adicionales

    assert merge([], []) == []
    assert merge([2, 3], []) == [2, 3]
    assert merge([], [2, 3]) == [2, 3]
    assert merge([6, 7, 10, 33], [5, 8, 9, 22]) == [5, 6, 7, 8, 9, 10, 22, 33]

    from os import path
    print(f"{path.basename(__file__)}: OK")


pruebas()
