# Se tiene un diccionario que guarda mensajes de un grupo, 
# donde cada elemento tiene como clave un identificador, 
# y como valor otro diccionario con la información del mensaje:

# {
# 	id: {
#		'de': nombre de usuario que escribió,
#		'texto': contenido del mensaje,
#		'respuesta_a_id': id del mensaje al cual responde, o 0 si no le responde a nadie
#	},
#	. . .
# }

# Escribir una función `contar_respuestas_a` que recibe el diccionario 
# de mensajes, una cadena `usuario_destino` y devuelva un nuevo diccionario 
# indicando la cantidad de respuestas que recibió por parte del resto 
# de los usuarios (la clave siendo el usuario, y valor la cantidad de respuestas).

# {
#   usuario1: x,
#   usuario2: y,
#   . . .
# }
#

# Escribir debajo de este comentario el código del ejercicio

def contar_respuestas_a(chat, persona):
	respuestas = {}
	for mensaje in chat.values():
		if mensaje['respuesta_a_id'] in chat: # el mensaje es una respuesta valida
			responde_a_mensaje_id = mensaje['respuesta_a_id']
			responde_a_mensaje_de = chat[responde_a_mensaje_id]['de']
			mensaje_de = mensaje['de']
			if responde_a_mensaje_de == persona:
				respuestas[mensaje_de] = respuestas.get(mensaje_de, 0) + 1
	return respuestas

# Pruebas
chat = {
	123: {
		'de': 'Pablo',
		'texto': 'Vieron el mail que mandé ayer?',
		'respuesta_a_id': 0
	},
	124: {
		'de': 'Juan',
		'texto': 'Todavía no',
		'respuesta_a_id': 123
	},
	125: {
		'de': 'Pablo',
		'texto': 'En cuanto antes, por favor',
		'respuesta_a_id': 124
	},
	126: {
		'de': 'Mateo',
		'texto': 'Yo ya lo lei!',
		'respuesta_a_id': 123
	},
	127: {
		'de': 'Juan',
		'texto': 'Perdón...',
		'respuesta_a_id': 125
	},
}

esperado = {
	'Juan': 2,
	'Mateo': 1
}

assert contar_respuestas_a(chat, 'Pablo') == esperado
