import sudoku
import random
from mapas import MAPAS

TEST_MODE = False #Esta linea sirve para desactivar test (ver final del archivo) <<<<<<<<<<<<<<<<<<<<<<<
COLOR_REST = "\x1b[0m"
COLOR_INPUT = "\x1b[36m"
COLOR_ROJO = "\x1b[31m"
COLOR_VERDE = "\x1b[32m"
INSTRUCCIONES = ('','valor','borrar','salir')

DESACTIVAR_COLORES = False #Esta linea sirve para desactivar los colores (no esta bien modificar constantes pero 🤷‍♂️) <<<<<<<<<<<<<<<<<<<<<<<
if DESACTIVAR_COLORES:
    COLOR_REST = ""
    COLOR_INPUT = ""
    COLOR_ROJO = ""
    COLOR_VERDE = ""
    #Estoy modificando constantes pero en realidad este comportamiento no depende en absoluto de la ejecucion del programa
    #y no hay ninguna logica del mismo arriba tampoco asi que no me parece mal hacerlo
    #Solo se estan cambiando al inicio de todo una sola vez antes de que pase nada

MENSAJE_INICIAL = COLOR_INPUT+"¿Qué desea hacer?"+COLOR_REST
MENSAJE_SIN_MOVIMIENTOS = COLOR_ROJO+"¡Cuidado, no hay movimientos posibles! Vas a tener que cambiar algo"+COLOR_REST
MENSAJE_TERMINO = COLOR_VERDE+"¡Terminó el sudoku!"+COLOR_REST

INSTRUCCIONES_DEL_JUEGO = f"""{COLOR_VERDE}Reglas del sudoku{COLOR_REST}
Regla 1: hay que completar las casillas vacías con un solo número del 1 al 9
Regla 2: en una misma fila no puede haber números repetidos
Regla 3: en una misma columna no puede haber números repetidos
Regla 4: en una misma región no puede haber números repetidos
Regla 5: la solución de un sudoku es única
¿Como jugar?
Ingrese la acción a realizar con el nombre de la accion ej: 'instruccion: {COLOR_INPUT}valor{COLOR_REST}' o el número ej: 'instruccion: {COLOR_INPUT}1{COLOR_REST}':
Ej: {COLOR_INPUT}valor a2 8{COLOR_REST}
Ej: {COLOR_INPUT}valor{COLOR_REST}, posicion: {COLOR_INPUT}8B{COLOR_REST} valor: {COLOR_INPUT}5{COLOR_REST}
Ej: {COLOR_INPUT}1 A1{COLOR_REST}, valor: {COLOR_INPUT}4{COLOR_REST}
"""

PLANTILLA_SUDOKU = """
          1 2 3   4 5 6   7 8 9
        ╔═══════╦═══════╦═══════╗
      a ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ a
      b ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ b
      c ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ c
        ╠═══════╬═══════╬═══════╣
      d ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ d
      e ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ e
      f ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ f
        ╠═══════╬═══════╬═══════╣
      g ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ g
      h ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ h
      i ║ {} {} {} ║ {} {} {} ║ {} {} {} ║ i
        ╚═══════╩═══════╩═══════╝
          1 2 3   4 5 6   7 8 9
"""

PREGUNTA_INPUT_EN_JUEGO = """Instrucciones 
1. valor  | Ingresar un valor
2. borrar | Borar un valor
3. salir  | Salir del programa
Instrucción: """

PREGUNTA_INPUT_INICIAL = """Instrucciones 
1. nuevo | Iniciar nuevo juego
2. salir | Salir del programa
Instrucción: """

def borrar_consola():
    print('\033c') #lo saqué de internet, imprime un caracter especial en unicode que supongo limpia la consola
    print(COLOR_REST)


def obtener_texto_sudoku(sudoku_actual, sudoku_inicial):
    lista_numeros = []
    for fila in range(0,9):
        for columna in range(0,9):
            numero_cadena = ''

            if sudoku_inicial[fila][columna] == sudoku.VACIO:
                #Agregar color si es un valor nuevo que NO está en el original
                numero_cadena += COLOR_INPUT

            if sudoku_actual[fila][columna] != sudoku.VACIO:
                #Agregar numero a la lista
                numero_cadena += str(sudoku_actual[fila][columna])
            else:
                numero_cadena += ' '
            
            numero_cadena += COLOR_REST
            lista_numeros.append(numero_cadena)

    return PLANTILLA_SUDOKU.format(*lista_numeros)


def obtener_input_inicial():
    return input(PREGUNTA_INPUT_INICIAL).strip().lower()


def obtener_input_en_juego():
    return input(PREGUNTA_INPUT_EN_JUEGO).strip().lower()


def es_del_original(sudoku_inicial, fila, columna):
    if sudoku_inicial[fila][columna]: return True
    return False


def obtener_valor_posicion(valor = None):
    #Ej b4 -> 1,3
    #Ej A1 -> 0,0
    #Ej 5a -> 1,4
    #Es lo mismo mayuscula/minuscula y si primero letra o primero número
    posicion = valor or input("Valor a modificar (ej: A1): ").strip().lower()
    fila = -1
    columna = -1
    if len(posicion) != 2:
        return False
    
    if posicion[0].isdigit():
        columna = int(posicion[0]) - 1
        fila = ord(posicion[1]) - 97 #Convierte el valor de la letra en la tabla ascii a numero y le resta lo necesario para que quede la 'a' en la posicion 0
    elif posicion[1].isdigit():
        columna = int(posicion[1]) - 1
        fila = ord(posicion[0]) - 97

    if fila < 0 or fila > 8:
        return False

    if columna < 0 or columna > 8:
        return False

    return (fila,columna)


def obtener_numero(s, valor = None):
    valor = valor or input(s).strip()
    if len(valor) != 1 or not valor.isdigit() or valor == '0': return False
    return int(valor)


def procesar_instruccion(instruccion,sudoku_actual,sudoku_inicial):
    instruccion_lista = instruccion.split(' ')
    instruccion = instruccion_lista[0]
    parametro1 = len(instruccion_lista) > 1 and instruccion_lista[1]
    parametro2 = len(instruccion_lista) > 2 and instruccion_lista[2]

    if len(instruccion) == 1 and instruccion.isdigit(): instruccion = INSTRUCCIONES[int(instruccion)]
    if instruccion == 'salir':
        exit()

    elif instruccion == 'valor':
        return instruccion_insertar(instruccion,sudoku_actual,sudoku_inicial,parametro1,parametro2)

    elif instruccion == 'borrar':
        return instruccion_borrar(instruccion,sudoku_actual,sudoku_inicial,parametro1,parametro2)

    else:
        return sudoku_actual,COLOR_ROJO+'Ingrese una instrucción válida'+COLOR_REST


def instruccion_insertar(instruccion,sudoku_actual,sudoku_inicial,parametro1,parametro2):
    posicion = obtener_valor_posicion(parametro1) #Obtener/pedir posicion

    if posicion == False: #Comprobar posicion validad
        return sudoku_actual,COLOR_ROJO+'Posición incorrecta'+COLOR_REST

    if es_del_original(sudoku_inicial, *posicion): #Comprobar posicion que no sea del original
        return sudoku_actual,COLOR_ROJO+'Posición incorrecta'+COLOR_REST

    nuevo_valor = obtener_numero("Nuevo valor: ", parametro2)
    if nuevo_valor == False:
        return sudoku_actual,COLOR_ROJO+'Valor inválido'+COLOR_REST

    if not sudoku.es_movimiento_valido(sudoku_actual,posicion[0],posicion[1],nuevo_valor):
        return sudoku_actual,COLOR_ROJO+'Movimiento inválido'+COLOR_REST

    nuevo_sudoku = sudoku.insertar_valor(sudoku_actual,posicion[0],posicion[1],nuevo_valor)
    return nuevo_sudoku,MENSAJE_INICIAL


def instruccion_borrar(instruccion,sudoku_actual,sudoku_inicial,parametro1,parametro2):
    posicion = obtener_valor_posicion(parametro1) #Obtener/pedir posicion

    if posicion == False: #Comprobar posicion validad
        return sudoku_actual,COLOR_ROJO+'Posición incorrecta'+COLOR_REST

    if es_del_original(sudoku_inicial, *posicion): #Comprobar posicion que no sea del original
        return sudoku_actual,COLOR_ROJO+'Posición incorrecta'+COLOR_REST

    nuevo_sudoku = sudoku.borrar_valor(sudoku_actual,posicion[0],posicion[1])
    return nuevo_sudoku,MENSAJE_INICIAL


def mapa_ramdom():
    return random.choice(MAPAS)


def crear_sudokus():
    mapa = mapa_ramdom()
    if TEST_MODE:
        mapa = MAPAS[29]
    sudoku_inicial = sudoku.crear_juego(mapa)
    sudoku_actual = sudoku.crear_juego(mapa)
    return sudoku_inicial,sudoku_actual


def main():
    sudoku_inicial = None
    sudoku_actual = None
    jugando = False
    mensaje = MENSAJE_INICIAL

    while True:
        borrar_consola()
        if sudoku_actual:
            texto_sudoku = obtener_texto_sudoku(sudoku_actual,sudoku_inicial)
            print(texto_sudoku) #Mostrar sudoku
        else:
            print(INSTRUCCIONES_DEL_JUEGO) #Mostrar instrucciones del juego por única vez

        #Comprobar si se terminó el sudoku
        if jugando and sudoku.esta_terminado(sudoku_actual):
            mensaje = MENSAJE_TERMINO
            jugando = False
        #Comprobar si hay movimientos posibles
        elif jugando and not sudoku.hay_movimientos_posibles(sudoku_actual):
            if mensaje == MENSAJE_INICIAL:
                mensaje = ""
            else:
                mensaje += "\n"
            mensaje += MENSAJE_SIN_MOVIMIENTOS
            

        print(mensaje) #Mostrar mensaje

        if jugando:
            instruccion = obtener_input_en_juego() #Mostrar y pedir instruccion
            nuevo_sudoku,mensaje = procesar_instruccion(instruccion,sudoku_actual,sudoku_inicial)
            sudoku_actual = nuevo_sudoku

        else:
            instruccion = obtener_input_inicial().lower().strip() #Mostrar y pedir instruccion
            if instruccion == 'nuevo' or instruccion == '1':
                sudoku_inicial,sudoku_actual = crear_sudokus()
                jugando = True
                mensaje = MENSAJE_INICIAL

            if instruccion == 'salir' or instruccion == '2':
                exit()

main()


"""
TEST
Solucion MAPAS[29]

#nota: para probar si no hay movimientos posibles usar valor A2 8

valor A2 9
valor A3 8
valor A4 1
valor A5 7
valor A6 5
valor A7 6
valor A8 4
valor A9 3
valor B1 6
valor B2 5
valor B3 7
valor B4 3
valor B5 9
valor B6 4
valor B7 1
valor B8 2
valor B9 8
valor C1 1
valor C2 3
valor C3 4
valor C4 2
valor C5 8
valor C6 6
valor C7 5
valor C8 7
valor C9 9
valor D1 8
valor D2 2
valor D3 1
valor D4 6
valor D5 4
valor D6 9
valor D7 7
valor D8 3
valor D9 5
valor E1 5
valor E2 7
valor E3 3
valor E4 8
valor E5 2
valor E6 1
valor E7 4
valor E8 9
valor E9 6
valor F1 4
valor F2 6
valor F3 9
valor F4 7
valor F5 5
valor F6 3
valor F7 2
valor F8 8
valor F9 1
valor G1 3
valor G2 1
valor G3 2
valor G4 4
valor G5 6
valor G6 8
valor G7 9
valor G8 5
valor G9 7
valor H1 7
valor H2 8
valor H3 5
valor H4 9
valor H5 1
valor H6 2
valor H7 3
valor H8 6
valor H9 4
valor I1 9
valor I2 4
valor I3 6
valor I4 5
valor I5 3
valor I6 7
valor I7 8
valor I8 1


// JAVASCRIPT
// PROBADOR AUTOMATICO DE SUDOKUS

// ENTRAR A: http://www.sudokumania.com.ar/sm1/sudoku-solucionar/solucionar.php
// LLENAR Y RESOLVER
// TOCAR F12 o click derecho inspeccionar elemento
// Buscar la opcion que dice Console
// Pegar este código y darle a enter
//(si, lo hice yo el código)

let rows = document.querySelector('table.tabla').children[0].children
let instructions = ''
let y = 0
let letras = ['A','B','C','D','E','F','G','H','I']
for(const row of rows){
    let x = 1
    for(cell of row.children){
        const valor = cell.children[0].value
        const fila = y+""
        const columna = x+""
        const letra_fila = letras[y]
        const letra_columna = letras[x]

        //ESTA LINEA ES LA QUE HAY QUE CAMBIAR PARA QUE ANDE SEGUN EL MODELO DE SUDOKU
        instructions += "valor "+letra_fila+columna+" "+valor
        //FIN DE ESA LINEA

        instructions += '\n'
        x++
    }
    y++
}
console.log(instructions)
"""