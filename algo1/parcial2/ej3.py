# Se pide implementar una clase `Semaforo` con tres luces (roja, amarilla y verde) 
# y el siguiente comportamiento:

# - Al instanciar la clase se debe ver la luz roja prendida.​

# - Debe tener un metodo `siguiente` para apagar la luz actual y encender la siguiente 
# (el orden de encendido de las luces es `roja->amarilla->verde->roja->amarilla->...`)

# - Debe tener un metodo `apagar` que apague el semaforo. En un semaforo apagado todas las 
# luces estan apagadas y no se puede encender ninguna. Si se intenta usar el metodo 
# `siguiente` mientras el semaforo esta apagado se debe lanzar una excepcion del tipo ValueError.

# - Debe tener un metodo `encender` que encienda el semaforo. Al encender el semaforo 
# el estado de las luces debe ser el mismo que tenia antes de apagarlo.

# - Al imprimir una instancia de la clase semaforo, debe mostrar qué luz esta prendida. 
# Si el semaforo esta apagado, debe mostrar que esta apagado.

# La representacion interna de la clase es a criterio pero debe ser acorde al comportamiento y no agregar complejidad.


# Escribir debajo de este comentario el cdigo del ejercicio

class Semaforo:
    ROJA = 'roja'
    AMARILLA = 'amarilla'
    VERDE = 'verde'
    ESTADOS = (ROJA, AMARILLA, VERDE)
    
    def __init__(self):
        self.predido = True
        self.estado = 0

    def siguiente(self):
        if not self.predido:
            raise ValueError()
        self.estado = (self.estado + 1) % len(self.ESTADOS)

    def encender(self):
        self.predido = True

    def apagar(self):
        self.predido = False

    def __str__(self):
        return self.ESTADOS[self.estado]

# Pruebas

s = Semaforo()
assert 'roja' in str(s)
s.siguiente()
assert 'amarilla' in str(s)
s.siguiente()
assert 'verde' in str(s)
s.siguiente()
assert 'roja' in str(s)
s.apagar()
hay_excepcion = True
try:
    s.siguiente()
    hay_excepcion = False
except ValueError:
    pass
assert hay_excepcion, "excepcion no fue lanzada"
s.encender()
assert 'roja' in str(s)
s.siguiente()
assert 'amarilla' in str(s)
