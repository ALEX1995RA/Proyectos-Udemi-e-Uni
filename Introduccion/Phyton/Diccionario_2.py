# iniciar un diccionario vasio
jugador = {}
print(jugador)
jugador['nombre'] = 'Alex'
jugador['puntaje'] = 0
print(jugador)

jugador['puntaje'] = 200
print(jugador)

print(jugador.get('consola', 'No Existe ese valor'))

#Iterar
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#eliminar
del jugador ['nombre']
del jugador ['puntaje']
print(jugador)