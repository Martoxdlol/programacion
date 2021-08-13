def agregar_a_comuna(comuna, dni):
    with open(f"{comuna}.csv", 'a') as f:
        f.write(dni+'\n')


def extraer_distritos(todos):
    comunas = set()
    with open("todos.csv") as f:
        for line in f:
            comuna, dni = line.rstrip().split(',')
            
            # Resetea el contenido del archivo si es que existe, o lo crea
            if not comuna in comunas:
                with open(f"{comuna}.csv", "w"):
                    pass
                comunas.add(comuna)
                
            agregar_a_comuna(comuna, dni)


def pruebas():
    extraer_distritos("todos.csv")

    # todos.csv contiene:
    # ---------
    # 12,345678
    # 15,456789
    # 12,123456
    # 12,234567
    # 15,123123

    # Se deberían haber creado dos archivos:
    #
    # 12.csv
    # ------
    # 345678
    # 123456
    # 234567
    #
    #
    # 15.csv
    # ------
    # 456789
    # 123123

    with open('12.csv') as f:
        assert f.read().strip() == '345678\n123456\n234567'
        
    with open('15.csv') as f:
        assert f.read().strip() == '456789\n123123'

    from os import path
    print(f"{path.basename(__file__)}: OK")


pruebas()
