cancion = {
    'artista' : 'Metalica',
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}
print(cancion['artista'])
print(cancion['lanzamiento'])

artista = cancion['artista']
print(f'estoy escuchando a {artista}')

print(cancion)

cancion['playlist'] = 'Heavy Metal'
print(cancion)

cancion['cancion'] = 'Seek Y Destroy'
print(cancion)

del cancion['lanzamiento']
print (cancion)