import vectores as math_r3

def area_triangulo(puntoA_x, puntoA_y, puntoA_z,   puntoB_x, puntoB_y, puntoB_z,   puntoC_x, puntoC_y, puntoC_z):
    """Recibe las coordenadas de tres puntos en R3 y devuelve el área del triángulo que conforman"""
    diferencia_AB_x, diferencia_AB_y, diferencia_AB_z = math_r3.diferencia(puntoA_x, puntoA_y, puntoA_z,   puntoB_x, puntoB_y, puntoB_z)
    diferencia_AC_x, diferencia_AC_y, diferencia_AC_z = math_r3.diferencia(puntoA_x, puntoA_y, puntoA_z,   puntoC_x, puntoC_y, puntoC_z)
    producto_vectorial_AB_AC_x, producto_vectorial_AB_AC_y, producto_vectorial_AB_AC_z = math_r3.producto_vectorial(diferencia_AB_x, diferencia_AB_y, diferencia_AB_z,   diferencia_AC_x, diferencia_AC_y, diferencia_AC_z)
    norma = math_r3.norma(producto_vectorial_AB_AC_x, producto_vectorial_AB_AC_y, producto_vectorial_AB_AC_z)
    return norma/2

#Nota: si usasemos tuplas se haría todo mas legible el código pero no las vimos todavía así que creo que no debería usarlas

def _test(x1, y1, z1,   x2, y2, z2,   x3, y3, z3, resultado_esperado, nombre_del_test = ""):
    test = area_triangulo(x1, y1, z1,   x2, y2, z2,   x3, y3, z3)
    print("Test", nombre_del_test, test)
    assert round(test, 3) == resultado_esperado #Redondeamosa 3 decimales porque no conozco tantos decimales de la respuesta correcta

_test(5, 8, -1,   -2, 3, 4,   -3, 3, 0,   19.455, "1")
_test(2, 2, -3.4,   1, 4, -5,   -4, -2.2, 2,   11.226, "2")
_test(-4, -2.3, 5,   2, 7, -9,   2.6, -4, 53.48,   289.141, "3")

#La funcion test tiene el solo proposito de hacer varias pruebas de la funcion area_triangulo

# checkeado con https://es.planetcalc.com/218/


################################## CON TUPLAS ####### Esto está demas pero lo pongo porque está bueno

def area_triangulo(puntoA_x, puntoA_y, puntoA_z,   puntoB_x, puntoB_y, puntoB_z,   puntoC_x, puntoC_y, puntoC_z):
    """Recibe las coordenadas de tres puntos en R3 y devuelve el área del triángulo que conforman"""
    diferencia_AB = math_r3.diferencia(puntoA_x, puntoA_y, puntoA_z,   puntoB_x, puntoB_y, puntoB_z)
    diferencia_AC = math_r3.diferencia(puntoA_x, puntoA_y, puntoA_z,   puntoC_x, puntoC_y, puntoC_z)
    producto_vectorial_AB_AC = math_r3.producto_vectorial(*diferencia_AB, *diferencia_AC)
    norma = math_r3.norma(*producto_vectorial_AB_AC)
    return norma/2