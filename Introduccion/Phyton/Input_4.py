Playlist = {}
Playlist['Canciones'] = []
def app ():
    Agregar_Playlist = True
    while Agregar_Playlist:
        Nombre_Playlist = input ('Como desase Nombrar a tu Playlist?\r\n') 
        if Nombre_Playlist:
          Playlist['Nombre'] = Nombre_Playlist
          Agregar_Playlist = False
          Agregar_Canciones()
def Agregar_Canciones():
    Agregar_Cancion = True
    while Agregar_Cancion:
        Nombre_Playlist = Playlist['Nombre']
        pregunta = f'\r\n Agregar canciones para la playlist {Nombre_Playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar Canciones \r\n'
        Cancion = input(pregunta)
        if Cancion == 'X':
            print('Finalizando...')
        else:
            Playlist['Canciones'].append(Cancion)
            print(Playlist)
            Mostrar_resumen()
def Mostrar_resumen():
    Nombre_Playlist = Playlist['Nombre']
    print(f'Playlist: {Nombre_Playlist}\r\n')   
    print('Canciones:\r\n') 
    for cancion in Playlist['Canciones']:   
        print(cancion)  


app()        