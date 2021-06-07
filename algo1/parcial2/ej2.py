# Se tiene un archivo CSV de tres columnas llamado `operaciones.csv`. Las columnas son: 
#   - cuenta (cadena indicando el nombre de la cuenta) 
#   - operacion (tipo de la operación: `“extraccion”` o `“deposito”`)
#   - monto (valor de la operación, un entero positivo). 
# El archivo no tiene errores, está ordenado por el campo “Cuenta” y tiene encabezado con 
# el nombre de cada columna.

# Se pide escribir una funcion `calcular_balances` que genere un archivo `balances.csv` 
# con el balance de cada cuenta tras procesar las operaciones 
# presentes en el archivo `operaciones.csv`. 
# El archivo debe tener el formato y encabezado `cuenta,balance`. 

# Notas: 
# - Se debe asumir un balance inicial de 0. 
# - Las extracciones restan al valor del balance y los depósitos suman al mismo,  y si se desea 
# realizar una extraccion de mas plata que el monto disponible, la operacion no se realiza. 
# - Al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos 
# abiertos deben quedar cerrados.


# Escribir debajo de este comentario el código del ejercicio

import csv

ARCHIVO_OPERACIONES = "operaciones.csv"
ARCHIVO_BALANCES = "balances.csv"

OPERACION_EXTRACCION = "extraccion"
OPERACION_DEPOSITO = "deposito"

KEY_CUENTA = "cuenta"
KEY_OPERACION = "operacion"
KEY_MONTO = "monto"

def calcular_balances():
    balances = {}
    with open(ARCHIVO_OPERACIONES, newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for operacion in reader:
            cuenta = operacion[KEY_CUENTA]
            accion = operacion[KEY_OPERACION]
            monto = int(operacion[KEY_MONTO])
            balances[cuenta] = balances.get(cuenta, 0)

            if accion == OPERACION_DEPOSITO:
                balances[cuenta] += monto
            elif accion == OPERACION_EXTRACCION and balances[cuenta] >= monto:
                balances[cuenta] -= monto

    with open(ARCHIVO_BALANCES, 'w') as archivo_balances:
        for cuenta,monto in balances.items():
            archivo_balances.write(f"{cuenta},{monto}\n")


# Pruebas

calcular_balances()

with open('balances.csv') as f:
    lineas = f.read().splitlines()
    assert 'Cuenta de Nora,27' in lineas
